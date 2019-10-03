---
layout: post
title: 如何修复升级到 macOS Sierria 后命令行工具失效问题
subtitle: "一种简单的方式修复升级到 macOS Sierria 后命令行工具失效问题（ xcrun: error: invalid active developer path ）"
date: 2016-10-08 09:00:00
author: "Shiny"
header-img: "assets/img/post-macOS-Sierria-fallback_screen_large.jpg"
catalog: true
tags:
    - macOS
    - shell

---

## 问题表现

 升级了 macOS Sierria 后，一直用起来非常舒畅。但今天想更新一下项目代码库时突然告诉我说：

```shell
Shinys-MacBook-Pro:~ shinyzhu$ svn
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

如图：

![post-macOS-Sierria-cmd-tools-1](/assets/img/post-macOS-Sierria-cmd-tools-1.png)

## 修复步骤

这个问题的原因是升级系统后，命令行工具被干掉了（我就说怎么原来剩余空间一直报警，现在有24G剩余空间了）

修复方式很简单，在命令行输入：

```shell
Shinys-MacBook-Pro:~ shinyzhu$ xcode-select --install
```

会出现一个对话框，选择下载就会为你下载命令行工具了，如图：

 ![post-macOS-Sierria-cmd-tools-2](/assets/img/post-macOS-Sierria-cmd-tools-2.png)

 等待完成即可使用`svn`，`git`了：

```shell
Shinys-MacBook-Pro:MCP shinyzhu$ svn status
svn: E155036: Please see the 'svn upgrade' command
svn: E155036: The working copy at '/Users/shinyzhu/Projects/MCP'
is too old (format 29) to work with client version '1.9.4 (r1740329)' (expects format 31). You need to upgrade the working copy first.

Shinys-MacBook-Pro:MCP shinyzhu$ svn upgrade
Upgraded '.'
Shinys-MacBook-Pro:MCP shinyzhu$ svn status
```

`svn`需要来一次`svn upgrade`升级版本。

> 注：xcode-select —install 只是安装命令行工具，不会安装 xcode