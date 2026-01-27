# -*- coding: utf-8 -*-
"""
HIFINI 免抓包签到脚本（2026年1月最终优化版）
修复结果误判问题，签到成功正常提示
"""
import requests
import sys
import json

requests.packages.urllib3.disable_warnings()

# 兼容通知模块（青龙/本地都能用）
try:
    from notify import send
except ImportError:
    def send(title, content):
        """本地打印通知，格式和青龙一致"""
        print(f"\n【{title}】\n{content}\n")

def print_step(step, msg):
    """带步骤的日志，清晰看到执行过程"""
    print(f"\n===== 步骤{step}：{msg} =====")

def hifini_sign():
    print_step(1, "启动HIFINI最新签到脚本（优化版）")
    
    # ======================
    # 你的Cookie（填写你自己的cookies）
    # ======================
    COOKIE = ""

    if not COOKIE:
        print_step(1, "❌ 请先填写你的Cookie！")
        send("HIFINI 签到失败", "未配置有效Cookie，任务终止")
        return
    print_step(1, "✅ Cookie加载完成")

    # 2026年1月实测有效 - 签到接口/请求头/参数
    SIGN_URL = "https://hifiti.com/sg_sign.htm"
    HEADERS = {
        'Cookie': COOKIE,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Referer': 'https://hifiti.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    SIGN_DATA = {
        "action": "sign",
        "inajax": "1"
    }

    # 执行签到核心逻辑
    try:
        print_step(2, "调用HIFINI签到接口...")
        resp = requests.post(
            SIGN_URL,
            headers=HEADERS,
            data=SIGN_DATA,
            timeout=30,
            verify=False
        )
        resp.encoding = 'utf-8'
        # 解析JSON返回结果，格式化输出
        result = json.loads(resp.text)
        result_text = json.dumps(result, ensure_ascii=False, indent=2)
        print_step(2, f"✅ 接口响应成功：\n{result_text}")

        # ======================
        # 核心优化：精准判断签到结果（兼容所有成功提示）
        # ======================
        code = result.get("code", "")
        message = result.get("message", "")
        if code == "0" and "成功签到" in message:
            # 签到成功：提取排名、金币等信息，提示更友好
            msg = f"✅ HIFINI签到成功！\n{message}"
        elif "已签到" in message or "今天已经签到" in message:
            # 重复签到：避免误判为异常
            msg = f"✅ HIFINI今日已签到！\n{message}"
        else:
            # 真正的异常情况
            msg = f"⚠️ HIFINI签到异常！\n错误码：{code}\n错误信息：{message}"
        
        # 打印结果+发送通知
        print_step(3, msg)
        send("HIFINI 签到结果", msg)

    # 捕获JSON解析失败（接口非JSON返回）
    except json.JSONDecodeError:
        msg = f"❌ 签到接口返回格式异常！\n返回内容：{resp.text}"
        print_step(2, msg)
        send("HIFINI 签到失败", msg)
    # 捕获网络/超时等异常
    except requests.exceptions.Timeout:
        msg = "❌ 签到请求超时！请检查网络或网站是否可访问"
        print_step(2, msg)
        send("HIFINI 签到失败", msg)
    except requests.exceptions.ConnectionError:
        msg = "❌ 网络连接失败！请检查你的网络配置"
        print_step(2, msg)
        send("HIFINI 签到失败", msg)
    # 捕获其他未知异常
    except Exception as e:
        msg = f"❌ 签到执行出错：{str(e)}"
        print_step(2, msg)
        send("HIFINI 签到失败", msg)

if __name__ == "__main__":
    print("===== HIFINI自动签到脚本（2026优化版）启动 =====")
    hifini_sign()
    print("\n===== 脚本执行结束 =====")
    sys.exit(0)