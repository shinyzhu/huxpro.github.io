---
layout: post
title: "面向Linux环境的.NET Core入门教程"
subtitle: "跟我一起在Linux平台开发和部署.NET Core应用"
date: 2018-03-10 20:17:00
author: "Shiny"
header-img: "assets/img/2018/disc-cover-1489083.jpg"
catalog: true
tags:
    - dotnet
    - core
    - docker
---

## 面向Linux环境的.NET Core入门教程

### 认识.NET Core

[.NET Framework](https://docs.microsoft.com/en-us/dotnet/)是微软的一套软件开发和运行框架，它只能运行在Windows操作系统上，可以用来开发WPF桌面应用、运行在IIS上的ASP.NET网站应用、Windows系统服务应用等。架构上包含一个通用语言运行时CLR、框架类库FCL和其上的多种应用模型。并且支持多种编程语言，包括C#、VB、F#等。

我们常常说的.NET代表了.NET Framework，但.NET的覆盖面正在越来越广，应该说包括了.NET Framework，再加上Mono、Unity和现在的.NET Core。

[.NET Core](https://github.com/dotnet/core)是由[.NET基金会](https://www.dotnetfoundation.org)维护的一套软件开发和运行框架，.NET基金会类似于Linux基金会，管理着多个开源项目，其中就包括了.NET Core。.NET Core是一套完全重写的.NET框架，它除了能运行在Windows里之外，还能在Linux和Mac OS X上运行。.NET Core的定位是跨平台、云应用优先，适应容器化和微服务平台。

本文以CentOS系统为例，介绍.NET Core SDK的安装和开发第一个.NET Core应用。

### 环境准备

```bash
shinyzhu@Shinys-MacBook-Pro ~> docker container run --name centdotnet -it centos bash
```

我们通过[下载分发包](https://www.microsoft.com/net/download/all)的方式来安装SDK。

```bash
[root@496b741d2fd2 opt]# curl -O https://download.microsoft.com/download/D/C/F/DCFA73BE-93CE-4DA0-AB76-98972FD6E475/dotnet-sdk-2.1.101-linux-x64.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
 55  152M   55 85.1M    0     0  2745k      0  0:00:57  0:00:31  0:00:26 1375k
```

```bash
[root@496b741d2fd2 opt]# dotnet --info
Failed to load ???, error: libunwind.so.8: cannot open shared object file: No such file or directory
Failed to bind to CoreCLR at '/opt/dotnet/shared/Microsoft.NETCore.App/2.0.6/libcoreclr.so'

Microsoft .NET Core Shared Framework Host

  Version  : 2.0.6
  Build    : 74b1c703813c8910df5b96f304b0f2b78cdf194d
```

报错信息因为没有库，需要执行：

```bash
[root@496b741d2fd2 /]# yum install libunwind libicu
```

完成之后即可：

```bash
[root@496b741d2fd2 /]# dotnet --info
.NET Command Line Tools (2.1.101)

Product Information:
 Version:            2.1.101
 Commit SHA-1 hash:  6c22303bf0

Runtime Environment:
 OS Name:     centos
 OS Version:  7
 OS Platform: Linux
 RID:         centos.7-x64
 Base Path:   /opt/dotnet/sdk/2.1.101/

Microsoft .NET Core Shared Framework Host

  Version  : 2.0.6
  Build    : 74b1c703813c8910df5b96f304b0f2b78cdf194d
```

### 创建项目

使用命令行新建项目：

```bash
[root@496b741d2fd2 projects]# dotnet new console -o ConsoleApp

Welcome to .NET Core!
---------------------
Learn more about .NET Core @ https://aka.ms/dotnet-docs. Use dotnet --help to see available commands or go to https://aka.ms/dotnet-cli-docs.

Telemetry
--------------
The .NET Core tools collect usage data in order to improve your experience. The data is anonymous and does not include command-line arguments. The data is collected by Microsoft and shared with the community.
You can opt out of telemetry by setting a DOTNET_CLI_TELEMETRY_OPTOUT environment variable to 1 using your favorite shell.
You can read more about .NET Core tools telemetry @ https://aka.ms/dotnet-cli-telemetry.

Configuring...
-------------------
A command is running to initially populate your local package cache, to improve restore speed and enable offline access. This command will take up to a minute to complete and will only happen once.
Decompressing 100% 10145 ms
Expanding 100% 54807 ms
Getting ready...
The template "Console Application" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on ConsoleApp/ConsoleApp.csproj...
  Restoring packages for /opt/projects/ConsoleApp/ConsoleApp.csproj...
  Generating MSBuild file /opt/projects/ConsoleApp/obj/ConsoleApp.csproj.nuget.g.props.
  Generating MSBuild file /opt/projects/ConsoleApp/obj/ConsoleApp.csproj.nuget.g.targets.
  Restore completed in 386.37 ms for /opt/projects/ConsoleApp/ConsoleApp.csproj.

Restore succeeded.
```

Developing .NET Core app on Linux - Preparations