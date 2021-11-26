from flask import Flask, render_template
app=Flask(__name__)
app.config['SECRET_KEY'] = "jkbabv03oe42gbleknvperbfrenep"
@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5656
    )