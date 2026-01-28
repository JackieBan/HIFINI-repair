## HIFINI 音乐磁场签到脚本（2026年1月最终优化版）

首先感谢[fengwenhua](https://github.com/fengwenhua/hifini_sign_in)大佬和[KunCheng-He](https://github.com/KunCheng-He/hifini-sign-in?tab=readme-ov-file)大佬提供的代码，在很长一段时间无私贡献脚本进行使用，此版本是在网站进行迁移后解决脚本失效和优化签到结果输出[HIFINI](https://hifiti.com/)

#### 核心优化：

1. **精准结果判断：** 适配接口返回的 **code:0** +  **成功签到！** 提示，不再只识别`签到成功`，彻底解决误判
2. **JSON 格式化解析：** 接口返回的是 JSON 数据，直接解析后提取 code 和 message，输出更整洁
3. **友好提示：** 签到成功后直接显示==排名==、==金币奖励==，无需额外查看原始返回
4. **兼容重复签到：** 如果重复点击签到，会提示今日已签到，不会误判为异常
5. **新增异常捕获：** 处理接口返回非 JSON 的情况，报错信息更精准

### 青龙面板使用步骤

1. 青龙面板创建订阅，然后复制以下命令到名称中：

`ql repo https://github.com/JackieBan/HIFINI-repair.git "hifini.py" "" ""`

<img width="1874" height="962" alt="image" src="https://github.com/user-attachments/assets/d725a8e8-0f1c-409b-8ee8-625f643e6687" />


2.添加依赖：

<img width="1874" height="962" alt="image" src="https://github.com/user-attachments/assets/7fdeaf54-b268-49e5-a629-7c05e9c3ffbc" />


3.运行订阅：

<img width="1874" height="962" alt="image" src="https://github.com/user-attachments/assets/25e60894-438c-4d5b-9b36-dd5e0cac8f47" />


4.查找cookie变量：

在官网F12，按照图中所示找到相对应位置：网络--文档，按ctrl+R，进行刷新，第一行便是cookie的位置，进行全部复制

<img width="798" height="758" alt="image" src="https://github.com/user-attachments/assets/647edf94-8f6b-4fbb-8053-d7e1f8b84205" />


5.填写cookie变量：

回到青龙面板，填写完毕后进行保存，即可等待运行（第一次在定时任务找到此任务手动运行进行检查）

<img width="1874" height="962" alt="image" src="https://github.com/user-attachments/assets/7023f0c7-5962-4c5e-9638-e9891a139ba2" />
