---
title: 'sublime快捷键和设置配置'
date:       2019-09-17
subtitle: 'jetbrains习惯'
tags:
	- ide
	- solution
	- sublime
	
---

### 起步
很多小伙伴使用jetbrains系列的编辑器后,在使用轻量级的sublime,可能会有一些设置和快捷键习惯不适应  
小编今天就给大家一些常用的sublime设置和快捷键的配置



### 设置
```
{
    // 颜色主题
    "color_scheme": "Packages/Color Scheme - Default/Monokai.sublime-color-scheme",
    // 自动保存
    "expand_tabs_on_save": true,
    // 字体大小
    "font_size": 18,
    
    "ignored_packages":
    [
        "Vintage"
    ],
    "save_on_focus_lost": true,
    // 制表符宽度
    "tab_size": 4,
    // 主题
    "theme": "Default.sublime-theme",
    // 自动转换为空格
    "translate_tabs_to_spaces": true,
    // 自动换行
    "word_wrap":true,
    // 设置不检查更新
    "update_check":false,
}

```

### 快捷键
```

[
    // 选取相同的单词
    { "keys": ["ctrl+shift+d"], "command": "find_under_expand" },
    // 快速复制一行
    { "keys": ["ctrl+d"], "command": "duplicate_line" },
    // 运行
    { "keys": ["ctrl+shift+f10"], "command": "build" },
    // 小换行
    { "keys": ["shift+enter"], "command": "run_macro_file", "args": {"file": "res://Packages/Default/Add Line.sublime-macro"} },
    // 重复上一个动作
    { "keys": ["ctrl+shift+k"], "command": "redo_or_repeat" },
    // 删除当前行
    { "keys": ["ctrl+y"], "command": "run_macro_file", "args": {"file": "res://Packages/Default/Delete Line.sublime-macro"} },

    // 带输入栏 运行python 程序
    { "keys": ["ctrl+f10"], "caption": "SublimeREPL:Python", 
                      "command": "run_existing_window_command", "args":
                      {
                           "id": "repl_python_run",
                           "file": "config/Python/Main.sublime-menu"
                      } 
    },
    // 查找替换
    { "keys": ["ctrl+r"], "command": "show_panel", "args": {"panel": "replace", "reverse": false} },
    // 交换快捷键
    { "keys": ["ctrl+h"], "command": "show_overlay", "args": {"overlay": "goto", "text": "@"} },
    // prettify中的代码格式化
    // { "keys": ["ctrl+shift+h"], "command": "replace_next" },
    // prettify 修改
    { "keys": ["ctrl+alt+l"], "command": "htmlprettify" },
    
]
```
### 找不到设置的[同学](https://caoyang7.github.io/)看这里

在sublime菜单栏中点击Preferences(首选项)->settings(设置)  
在sublime菜单栏中点击Preferences(首选项)->key bindings(快捷键)

![sublime_setting](/img/posts/ide/sublime_settings.png)

如图,左边的是默认设置,在右边粘贴你的设置配置代码即可

![sublime_setting](/img/posts/ide/sublime_settings2.png)

如图,左边的是默认快捷键,在右边粘贴你的自定义快捷键即可

![sublime_setting](/img/posts/ide/sublime_settings3.png)