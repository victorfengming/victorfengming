---
title: "Vue CLI的安装"
cover: "/img/lynk/13.jpg"
date:       2019-09-17
tags:
	- web
	- vue
	- solution
---

<div class="warning custom-block"><p class="custom-block-title">关于旧版本</p> <p>Vue CLI 的包名称由 <code>vue-cli</code> 改成了 <code>@vue/cli</code>。
如果你已经全局安装了旧版本的 <code>vue-cli</code> (1.x 或 2.x)，你需要先通过 <code>npm uninstall vue-cli -g</code> 或 <code>yarn global remove vue-cli</code> 卸载它。</p></div>

<div class="tip custom-block"><p class="custom-block-title">Node 版本要求</p> <p>Vue CLI 需要 <a href="https://nodejs.org/" target="_blank" rel="noopener noreferrer">Node.js<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg></a> 8.9 或更高版本 (推荐 8.11.0+)。你可以使用 <a href="https://github.com/creationix/nvm" target="_blank" rel="noopener noreferrer">nvm<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg></a> 或 <a href="https://github.com/coreybutler/nvm-windows" target="_blank" rel="noopener noreferrer">nvm-windows<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg></a> 在同一台电脑中管理多个 Node 版本。</p></div>

<p>可以使用下列任一命令安装这个新的包：</p>

<div class="language-bash extra-class"><pre class="language-bash"><code><span class="token function">npm</span> <span class="token function">install</span> -g @vue/cli
<span class="token comment"># OR</span>
<span class="token function">yarn</span> global <span class="token function">add</span> @vue/cli
</code></pre></div>

<p>安装之后，你就可以在命令行中访问 <code>vue</code> 命令。你可以通过简单运行 <code>vue</code>，看看是否展示出了一份所有可用命令的帮助信息，来验证它是否安装成功。</p>

<p>你还可以用这个命令来检查其版本是否正确 (3.x)：</p>

<div class="language-bash extra-class"><pre class="language-bash"><code>vue --version
</code></pre></div>

如果显示出了版本号的信息,即表示vue安装成功

![vue-v](/img/posts/vue/vuejs3.png)

