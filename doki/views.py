from doki.Calculator.views import Calculatorr
from doki import app
from doki.master.views import bluemaster

app.register_blueprint(Calculatorr)
app.register_blueprint(bluemaster)

if __name__ == "__main__":
    app.run(debug=True)
