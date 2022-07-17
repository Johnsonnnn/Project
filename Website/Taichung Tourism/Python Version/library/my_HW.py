from flask import Flask, request, render_template, url_for
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def choice_main():
    file1 = open('library/static/json/服務中心.json', 'r', encoding='utf-8-sig')
    # file1 = open('library/static/json/test.json', 'r', encoding='utf-8')

    center_data = json.load(file1)["ROOT"]["RECORD"]
    # print(center_data)
    return render_template('index.html', center_data=center_data)

@app.route('/choice1', methods=['GET'])#景點
def choice1():
    if request.method == 'GET':
        file2 = open('library/static/json/景點.json', 'r', encoding='utf-8-sig')
        attraction_data = json.load(file2)["ROOT"]["RECORD"]

        if request.args.get('page'):
            page = int(request.args.get('page'))
        else:
            page = 1
        if len(attraction_data) % 15 == 0:
            max_page = len(attraction_data) / 15
        elif len(attraction_data) % 15 > 0:
            max_page = len(attraction_data) // 15 + 1

        if page > max_page or page < 1:
            return render_template('routing/404.html')

        attraction_data = attraction_data[(page - 1) * 15 : page * 15]

        return render_template('data/attractions.html', center_data=attraction_data, page=page, max_page=max_page)

@app.route('/choice1/detail', methods=['GET'])#景點
def choice1_detail():
    if request.method == 'GET':
        file2 = open('library/static/json/景點.json', 'r', encoding='utf-8-sig')
        attraction_data = json.load(file2)["ROOT"]["RECORD"]
        if request.args.get('page'):
            page = int(request.args.get('page'))
        else:
            page = 1
        max_page = len(attraction_data)
        if page > max_page or page < 1:
            return render_template('routing/404.html')

        if request.args.get('ID'):
            count = 0 
            ID = request.args.get('ID')
            for i in attraction_data:
                if i["ID"] == ID:
                    break
                count += 1
            page = count + 1

        attraction_data = attraction_data[page - 1]
    return render_template('data/attractions_detail.html', center_data=attraction_data, page=page, max_page=max_page)

@app.route('/choice2')#低碳旅館
def choice2():
    file2 = open('library/static/json/低碳旅館.json', 'r', encoding='utf-8-sig')
    attraction_data = json.load(file2)["ROOT"]["RECORD"]

    return render_template('data/low_carbon_hotel.html', center_data=attraction_data)

@app.route('/choice2/detail', methods=['GET'])#低碳旅館
def choice2_detail():
    if request.method == 'GET':
        file2 = open('library/static/json/低碳旅館.json', 'r', encoding='utf-8-sig')
        attraction_data = json.load(file2)["ROOT"]["RECORD"]
        if request.args.get('page'):
            page = int(request.args.get('page'))
        else:
            page = 1
        max_page = len(attraction_data)
        if page > max_page or page < 1:
            return render_template('routing/404.html')

        attraction_data = attraction_data[page - 1]
    return render_template('data/low_carbon_hotel_detail.html', center_data=attraction_data, page=page, max_page=max_page)

@app.route('/choice3')#旅館
def choice3():
    file2 = open('library/static/json/旅館.json', 'r', encoding='utf-8-sig')
    attraction_data = json.load(file2)["ROOT"]["RECORD"]

    return render_template('data/hotel.html', center_data=attraction_data)

@app.route('/choice3/detail', methods=['GET'])#旅館
def choice3_detail():
    if request.method == 'GET':
        file2 = open('library/static/json/旅館.json', 'r', encoding='utf-8-sig')
        attraction_data = json.load(file2)["ROOT"]["RECORD"]
        if request.args.get('page'):
            page = int(request.args.get('page'))
        else:
            page = 1
        max_page = len(attraction_data)
        if page > max_page or page < 1:
            return render_template('routing/404.html')

        attraction_data = attraction_data[page - 1]
    return render_template('data/hotel_detail.html', center_data=attraction_data, page=page, max_page=max_page)

@app.route('/choice4')#民宿
def choice4():
    file2 = open('library/static/json/民宿.json', 'r', encoding='utf-8-sig')
    attraction_data = json.load(file2)["ROOT"]["RECORD"]

    return render_template('data/lodging.html', center_data=attraction_data)

@app.route('/choice4/detail', methods=['GET'])#民宿
def choice4_detail():
    if request.method == 'GET':
        file2 = open('library/static/json/民宿.json', 'r', encoding='utf-8-sig')
        attraction_data = json.load(file2)["ROOT"]["RECORD"]
        if request.args.get('page'):
            page = int(request.args.get('page'))
        else:
            page = 1
        max_page = len(attraction_data)
        if page > max_page or page < 1:
            return render_template('routing/404.html')

        attraction_data = attraction_data[page - 1]
    return render_template('data/lodging_detail.html', center_data=attraction_data, page=page, max_page=max_page)
