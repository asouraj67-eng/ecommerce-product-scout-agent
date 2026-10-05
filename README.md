# 海购选品助手

> OpenClaw Agent 配置 — 可用于任何兼容 OpenClaw 协议的 AI 产品

跨境电商选品研究助手，支持 Amazon、TikTok Shop、eBay、Shopee 等多平台。自动化数据采集、利润模型计算、六维评分体系，输出清晰的 Go / No-Go 选品决策。

## 核心能力

- 🔍 **多平台数据采集** — Amazon/TikTok Shop/eBay/Shopee/Lazada，支持 10+ 国家站点
- 💰 **利润模型计算** — 平台佣金 + FBA 物流 + 广告成本 + 退货率，自动测算利润空间
- 📊 **六维评分体系** — 需求强度、竞争烈度、利润空间、运营难度、风险等级、机会窗口
- ✅ **明确选品决策** — Strongly Recommend / Caution / Not Recommend，附决策理由
- 📁 **Excel 五表报告** — 执行摘要、原始数据、分析汇总、利润分析、机会排名
- 🔄 **批量关键词分析** — 多词并行分析，综合排名对比

---

## 🚀 零配置启动

以下能力**无需任何配置**即可使用：

> LLM 分析评分 · 利润模型计算 · 选品决策报告 · 批量关键词对比

数据采集依赖平台提供的 `browser` / `web-scraper` 工具。如平台支持这些工具，数据采集无需额外配置。

---

## ✨ 可选增强能力

### Firecrawl 网页抓取

**需要：** Firecrawl API Key（[免费注册](https://www.firecrawl.dev)）

在平台激活配置中填写 `FIRECRAWL_API_KEY`，或手动写入 `.secrets/scout-config.json`：

```json
{
  "firecrawl_api_key": "fc-your-api-key-here"
}
```

启用后可通过 Firecrawl 抓取动态页面、绕过反爬机制，提升数据采集成功率。

---

## 支持平台

| 电商平台 | 支持站点 |
|---------|---------|
| Amazon | US / DE / JP / UK / FR / IT / ES / CA / MX |
| TikTok Shop | US / UK / TH / VN / MY / SG / PH |
| eBay | US / UK / DE / AU |
| Shopee | TW / TH / VN / MY / SG / PH / ID |
| Lazada | TH / VN / MY / SG / PH / ID |

---

## 使用方式

```
你：分析一下 Amazon 美国站 yoga mat，预计采购成本 8-12 美元

助手：✅ 已收到！开始分析...
      平台：Amazon US | 关键词：yoga mat | 采购成本：$8-12
      预计耗时 3-5 分钟
```

快捷命令：
```
/analyze Amazon US yoga mat --cost 8-12 --price 25-40 --top 50
```




