
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# 部落格文章資料
posts = [
    {
        "title": "我的第一篇文章",
        "author": "小明",
        "content": "歡迎來到我的 Flask 部落格！"
    },
    {
        "title": "學習 Python",
        "author": "小華",
        "content": "今天開始學習 Python Flask。"
    }
]

# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 顯示單篇文章
@app.route("/post/<int:post_id>")
def post(post_id):
    if post_id < 0 or post_id >= len(posts):
        abort(404)

    return render_template("post.html", post=posts[post_id])


# 新增文章
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        content = request.form["content"]

        new_post = {
            "title": title,
            "author": author,
            "content": content
        }

        posts.append(new_post)

        return redirect(url_for("index"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
