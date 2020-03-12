---
title: Contribute
date: 2019-09-29 12:11:11
tags:
author: 程庆林
---

This guide is a comprehensive resource for contribute to [weshare](https://github.com/iweshare/weshare) - for both new and experienced contributors. If you got any good ideas, I welcome your contributions to weshare.

<!-- more -->

## Quick Reference

Here are the basic steps needed to get set up and contribute a patch. This is meant as a checklist, once you know the basics. For complete instructions please see the about page.

1. Install and set up `git` and other dependencies (see the about page for detailed information).
2. Fork the [weshare](https://github.com/iweshare/weshare) repository to your GitHub account and get the source code using.
   ```bash
   $ git clone https://github.com/<your_username>/weshare
   $ cd weshare
   ```
3. Install project node denpendencies:
   ```bash
   $ npm install
   ```
4. Run:
   ```bash
   $ npm run start
   ```
5. Browser the website [`http://localhost:4000/weshare`](http://localhost:4000/weshare) to check the blog.

## Create Your Post

I recommend to use [markdown](https://www.markdownguide.org/cheat-sheet/) to write the post, and all the site's posts are using markdown. Next, I will show you how to create your post. Let's dive into the details.

1. Use `hexo` command to create post:
   ```bash
   $ hexo new <your_post_title_name>
   ```
   After the command executed sucessfully, you can see <your_post_title_name>.md and the same name folder under the path `/source/_posts/'. Edit your post content in the markdown file, <your_post_title_name>.md, and once image or other file needed, put them under the same name folder as the post.
2. Create commit and push it.
   > Before you create commit, you need to generate static files first by using the following command.
   > ```bash
     $ npm run docs
     ```

   ```bash
   $ git add . && git commit -m 'Add a new post, <your_post_title_name>'
   $ git push -u origin master # make sure that the current branch is the lastest.
   ```
3. Create pull request to the [origin repository](https://github.com/iweshare/weshare). This is a basic usage of GitHub, I will not show the details.
   **I wish you do sync step to make your repository is the latest to the origin repository.**

**Good Luck!**