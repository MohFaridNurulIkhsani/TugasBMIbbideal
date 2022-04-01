from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/api/bmi/farid', methods=['POST'])
def bmi():
    duwur = float(request.form.get('duwur'))
    abot = float(request.form.get('abot'))
    BMI = abot / (duwur/100)
    msg = "BMI farid adalah " + str(BMI)
    if BMI <= 18.4:
        ket = "Anda Kurus."
    elif BMI <= 25:
        ket = "Anda Normal."
    elif BMI <= 40:
        ket = "Berlebihan."
    else:
        ket = "Kamu Berbahaya."
    hasil = {'sukses': 'true', 'msg': msg, 'ket': ket}
    return jsonify(hasil)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
