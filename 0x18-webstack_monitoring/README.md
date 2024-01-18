# 0x18. Webstack monitoring

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png" alt="Monitoring" />

## Tasks
#### 0. Sign up for Datadog and install datadog-agent
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240118%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240118T080300Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e4a42f756051937964c41313fce53c9f8a0f7f675f584f777a7e59cc0363e215" />
- Sign up for Datadog - Please make sure you are using the US website of Datagog (https://app.datadoghq.com)
- Use the US1 region
- Install datadog-agent on web-01
- Create an application key
- Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
- Your server web-01 should be visible in Datadog under the host name XX-web-01
- You can validate it by using this API
- If needed, you will need to update the hostname of your server

#### 1. Monitot some metrics
- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.

[2. Create a dashboard](https://github.com/alban-okoby/alx-system_engineering-devops/blob/master/0x18-webstack_monitoring/2-setup_datadog
) 
<br>
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

- Create a new dashboard
- Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
- Create the answer file **2-setup_datadog** which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API

