from flask import Flask, render_template, request, redirect, url_for, flash
from database import Dataset

def createApp():
    app = Flask(__name__)
    dataset = Dataset()

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/bar',methods=['GET','POST'])
    def bar():
        if request.method == 'POST':
            col_name = request.form['col_name']
            plot_file = "static/images/plotBar.png"
            dataset.plotBar(col_name).get_figure().savefig(plot_file)
            return render_template('bar.html', plot_file="images/plotBar.png")
        return render_template('bar.html')
    
    @app.route('/hist',methods=['GET','POST'])
    def hist():
        if request.method == 'POST':
            col_name = request.form['col_name']
            plot_file = "static/images/plotHist.png"
            dataset.plotHist(col_name).get_figure().savefig(plot_file)
            return render_template('hist.html', plot_file="images/plotHist.png")
        return render_template('hist.html')
    
    @app.route('/box',methods=['GET','POST'])
    def box():
        if request.method == 'POST':
            col_name1 = request.form['col_name1']
            col_name2 = request.form['col_name2']
            plot_file = "static/images/plotBox.png"
            dataset.plotBox(col_name1,col_name2).get_figure().savefig(plot_file)
            return render_template('box.html', plot_file="images/plotBox.png")
        return render_template('box.html')
    
    @app.route('/scatter',methods=['GET','POST'])
    def scatter():
        if request.method == 'POST':
            col_name1 = request.form['col_name1']
            col_name2 = request.form['col_name2']
            plot_file = "static/images/plotScatter.png"
            dataset.plotScatter(col_name1,col_name2).get_figure().savefig(plot_file)
            return render_template('scatter.html', plot_file="images/plotScatter.png")
        return render_template('scatter.html')
    
    return app

if __name__ == '__main__':
    app = createApp()
    app.run()