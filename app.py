from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")
	
@app.route("/services")
def services():
	return render_template("services.html")
	
@app.route("/team")
def team():
	return render_template("team.html")
	
@app.route("/sponsors")
def sponsors():
	return render_template("sponsors.html")
	
@app.route("/blog")
def blog():
	return render_template("blog.html")
	

#ERROR PAGES

#Not found error
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404
	
#Forbidden error
@app.errorhandler(403)
def forbidden(e):
	return render_template("403.html"), 403
	
#Internal server error
@app.errorhandler(500)
def internal_sv(e):
	return render_template("500.html"), 500



if __name__ == "__main__":
    app.run(debug=True)
