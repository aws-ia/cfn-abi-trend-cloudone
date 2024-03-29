---
weight: 9
title: Postdeployment options
description: Postdeployment options
---

## Verifying the solution functionality

Verifying the solution functionality depends on what modules and integrations you deployed in the previous step.

### Verifying CloudTrail analysis

1. Log in to your [Trend Cloud One](https://cloudone.trendmicro.com/home) account.
2. Choose [Integrations](https://cloudone.trendmicro.com/integrations/) at the bottom of the page and then [Trend Vision One](https://cloudone.trendmicro.com/integrations/vision-one) from the left-hand side of the page.
3. Verify that the status of AWS CloudTrail is **Connected**.
4. Log in to your [Vision One](https://portal.xdr.trendmicro.com/#/dashboard) account.
5. In the Trend Vision One console, navigate to XDR Threat Investigation > [Search](https://portal.xdr.trendmicro.com/#/app/search).
6. Change the search method to **Cloud Activity Data**.
7. Locate your CloudTrail data. For example, use the following search string: `*`
8. The presence of data means that the CloudTrail analysis deployed successfully.

### Verifying EC2 instance security agent deployment via SSM

1. Log in to your [Trend Cloud One](https://cloudone.trendmicro.com/home) account.
2. Choose [Endpoint & Workload Security](https://cloudone.trendmicro.com/workload/Application.screen?#dashboard), and then choose the [Computers](https://cloudone.trendmicro.com/workload/Application.screen?#computers_root) tab.
3. Verify that the **Agent Status Light Column** has a green indicator.
4. A green indicator means the agent deployed successfully.

**Next:** [Test the deployment](/test-deployment/index.html)
