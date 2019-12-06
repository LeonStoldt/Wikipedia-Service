from flask import Flask, request
import wikipediaapi

app = Flask(__name__)
wiki = wikipediaapi.Wikipedia('de')


@app.route('/')
def get_status():
    return 'WikipediaService is running'


@app.route('/api', methods=['POST'])
def receive_request():
    data = request.data
    page = wiki.page(data)

    if page.exists():
        page_title = page.title
        page_summary = page.summary
        url = page.fullurl
        message = '*{title}*\n{summary}\n\n{link}' \
            .replace('{title}', page_title) \
            .replace('{summary}', page_summary) \
            .replace('{link}', url)
    else:
        message = "Leider konnte ich kein passendes Ergebnis finden. Bitte überprüfe, ob du dich nicht vertippt hast."
    return message


if __name__ == '__main__':
    app.run(port=8095, debug=True)
