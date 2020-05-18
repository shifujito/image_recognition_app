from flask import Flask, render_template, request, redirect, url_for, session, make_response
import uuid
import os

from web_app.settings import DEBUG, HOST, PORT, BASE_DIR, PRODUCT_URL

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'web_app', 'templates'),
    static_folder=os.path.join(BASE_DIR, 'web_app', 'static'),
)
# ⇓ 本番環境では, 環境変数から取るようにする ⇓
app.secret_key = 'jskdjkfsakfjkldsajfdskafjdsk;a'


def get_base_context():
    return {
        'success_message': session.pop('success_message', None),
        'error_message': session.pop('error_message', None),
    }


@app.route('/')
def index():
    context = get_base_context()
    return render_template('index.html', **context)


@app.route('/estimate/', methods=['POST'])
def estimate():
    file = request.files.get('face_image')

    if file.filename == '':
        # ファイルが送られてきていないので, TOPへリダイレクトする
        session['error_message'] = 'ファイルをアップロードしてください'
        return redirect(url_for('index'))
    else:
        # ファイルを保存
        file = request.files.get('face_image')

        # 一意なファイル名 + 拡張子でOSに保存する
        filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
        file.save(os.path.join(BASE_DIR, 'web_app', 'static', 'image', filename))

        # 保存したファイルから機械学習モデルにかける
        # ロジックは, 未実装なので仮としておく

        # 仮の結果
        session['estimated_age'] = 23
        session['result_image_path'] = '/static/image/' + filename

        return redirect(url_for('result'))


@app.route('/result/')
def result():
    context = get_base_context()

    context.update({
        "product_url": PRODUCT_URL,
        "estimated_age": session['estimated_age'],
        "result_image_path": session['result_image_path']
    })

    return render_template('result.html', **context)


if __name__ == '__main__':
    app.run(
        debug=DEBUG,
        host=HOST,
        port=PORT
    )
