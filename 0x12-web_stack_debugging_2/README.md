# 0x12. Web stack debugging #2

[0. Run software as another user](https://github.com/alban-okoby/alx-system_engineering-devops/tree/master/0x12-web_stack_debugging_2/0-iamsomeoneelse)
For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:

- write a Bash script that accepts one argument
- the script should run the whoami command under the user passed as an argument
- make sure to try your script by passing different users


[1. Run Nginx as Nginx](https://github.com/alban-okoby/alx-system_engineering-devops/tree/master/0x12-web_stack_debugging_2/1-run_nginx_as_nginx)
mandatory
The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.

Fix this container so that Nginx is running as the nginx user.

Requirements:

- nginx must be running as nginx user
- nginx must be listening on all active IPs on port 8080
- You cannot use apt-get remove
- Write a Bash script that configures the container to fit the above requirements

[2. 7 lines or less](https://github.com/alban-okoby/alx-system_engineering-devops/tree/master/0x12-web_stack_debugging_2/100-fix_in_7_lines_or_less)
#advanced
Using what you did for task #1, make your fix short and sweet.

Requirements:

- Your Bash script must be 7 lines long or less
- There must be a new line at the end of the file
- You respect Bash script requirements
- You cannot use ;
- You cannot use &&
- You cannot use wget
- You cannot execute your previous answer file (Do not include the name of the previous script in this one)