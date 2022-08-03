from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)
game = GameOfLife(15, 15)
flag = True


@app.route('/')
def index():
    global game
    game = GameOfLife(15, 15)
    return render_template('index.html')


@app.route('/live')
def live():
    global game
    return render_template('live.html', game=game)


@app.route('/live')
def live_reboot():
    global game
    game = GameOfLife(15, 15)
    return render_template('live.html', game=game)

# new func


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
