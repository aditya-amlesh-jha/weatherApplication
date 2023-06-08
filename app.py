from flask import Flask, render_template, request, redirect, url_for, flash
from database import Dataset

def createApp():
    app = Flask(__name__)
    dataset = Dataset()

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/plotBar/<col_name>', methods=['GET'])
    def plotBar(col_name):
        plot_file = "static/images/plotBar.png"
        dataset.plotBar(col_name).get_figure().savefig(plot_file)
        return render_template('index.html', plot_file="images/plotBar.png")

    @app.route('/plotHist/<col_name>', methods=['GET'])
    def plotHist(col_name):
        plot_file = "static/images/plotHist.png"
        dataset.plotHist(col_name).get_figure().savefig(plot_file)
        return render_template('index.html', plot_file="images/plotHist.png")
    
    @app.route('/plotScatter/<col_name1>/<col_name2>', methods=['GET'])
    def plotScatter(col_name1,col_name2):
        plot_file = "static/images/plotScatter.png"
        dataset.plotScatter(col_name1,col_name2).get_figure().savefig(plot_file)
        return render_template('index.html', plot_file="images/plotScatter.png")
    
    @app.route('/plotBox/<col_name1>/<col_name2>', methods=['GET'])
    def plotBox(col_name1,col_name2):
        plot_file = "static/images/plotBox.png"
        dataset.plotBox(col_name1,col_name2).get_figure().savefig(plot_file)
        return render_template('index.html', plot_file="images/plotBox.png")
    
    return app

if __name__ == '__main__':
    app = createApp()
    app.run()