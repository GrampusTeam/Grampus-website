from flask import Flask, render_template, url_for, redirect, abort, escape
app = Flask(__name__)

################
#WEBSITE ROUTES#
################
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

#adding new routes:
@app.route("/security")
def security():
	return render_template("security.html")
	
@app.route("/hof")
def hof():
	return render_template("hof.html")

@app.route("/contribute")
def contribute():
	return render_template("contribute.html")
	
@app.route("/documentation")
def documentation():
	return render_template("documentation.html")
	
@app.route("/documentation/<document>")
def view_document(document):
	accepted_documents = ['plugins.html']
	for doc in accepted_documents:
		if document == doc:
			return render_template(document)
		else:
			abort(404)
	
#############
#ERROR PAGES#
#############

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



#############
#HONEY TRAPS#
#############

#Here start WORDPRESS honeytrap :P
@app.route('/blog/wp-includes/')
def wp_includes():
	abort(403)

@app.route('/blog/wp-admin/')
def wp_admin():
	abort(403)

@app.route('/blog/wp-content/')
def wp_content():
	return ""
	
@app.route('/blog/wp-content/<files>')
def wp_content_forb(files):
	return ""
	
@app.route('/blog/wp-includes/<directory>')
def wp_directory(directory):
	abort(403)

@app.route('/blog/wp-includes/<directory>/<fpd_file>')
def filedir_disclosure(directory, fpd_file):
	return "<br><b>Fatal error</b>:  Call to undefined function is_admin() in <b>/shared_1589479549852_home/GrampusAdministrator/public_html/blog/wp-includes/%s/%s</b> on line <b>20</b><br />" % (escape(directory), escape(fpd_file))

@app.route('/blog/wp-includes/<fpd_file>.php')
def file_disclosure(fpd_file):
	return "<br><b>Fatal error</b>:  Call to undefined function is_admin() in <b>/shared_1589479549852_home/GrampusAdministrator/public_html/blog/wp-includes/%s</b> on line <b>20</b><br />" % (escape(fpd_file))

#Here finish WORDPRESS honeytrap :P

if __name__ == "__main__":
    app.run(debug=True)
