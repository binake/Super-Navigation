from flask import Flask, request, jsonify
from flask_cors import CORS
from database import SessionLocal, init_db
from models import NavigationUrl
import random

app = Flask(__name__)
CORS(app)

def add_initial_urls():
    db = SessionLocal()
    
    # 检查是否已经有数据
    existing_urls = db.query(NavigationUrl).first()
    if existing_urls:
        db.close()
        return

    daily_urls = [
        {"name": "每日说晚", "url": "https://www.meiriwang.cn/", "category": "日常使用", "description": "60秒读懂世界"},
        {"name": "历史上的今天", "url": "https://www.lssdjt.com/", "category": "日常使用", "description": "精选历史事件"},
        {"name": "聚合阅读", "url": "https://www.juheyuedu.com/", "category": "日常使用", "description": "公众号文章聚合"},
        {"name": "资料论坛", "url": "https://www.ziliaobar.com/", "category": "日常使用", "description": "海量资料分享"}
    ]

    ai_urls = [
        {"name": "DeepSeek", "url": "https://www.deepseek.com/", "category": "AI", "description": "智能编程助手"},
        {"name": "ChatGPT Prompts", "url": "https://www.prompthero.com/", "category": "AI", "description": "ChatGPT提示词"},
        {"name": "AI图标", "url": "https://www.aicons.cn/", "category": "AI", "description": "AI生成Logo"},
        {"name": "火山写作", "url": "https://www.huoshanai.com/", "category": "AI", "description": "AI写作平台"}
    ]

    search_urls = [
        {"name": "搜索666", "url": "https://so.6soluo.com/", "category": "搜索引擎", "description": "聚合搜索引擎"},
        {"name": "百度", "url": "https://www.baidu.com/", "category": "搜索引擎", "description": "最大的中文搜索引擎"},
        {"name": "Google", "url": "https://www.google.com/", "category": "搜索引擎", "description": "全球最大搜索引擎"}
    ]

    all_urls = daily_urls + ai_urls + search_urls

    for url_data in all_urls:
        new_url = NavigationUrl(
            name=url_data['name'], 
            url=url_data['url'], 
            category=url_data['category'],
            description=url_data.get('description', '')
        )
        db.add(new_url)

    db.commit()
    db.close()

@app.route('/add_url', methods=['POST'])
def add_url():
    data = request.json
    db = SessionLocal()
    new_url = NavigationUrl(
        name=data['name'], 
        url=data['url'], 
        category=data['category'],
        description=data.get('description', '')
    )
    db.add(new_url)
    db.commit()
    db.close()
    return jsonify({"status": "success"})

@app.route('/get_urls', methods=['GET'])
def get_urls():
    db = SessionLocal()
    urls = db.query(NavigationUrl).all()
    db.close()
    return jsonify([{
        'id': url.id,
        'name': url.name,
        'url': url.url,
        'category': url.category,
        'description': url.description
    } for url in urls])

if __name__ == '__main__':
    init_db()
    add_initial_urls()  # 添加初始数据
    app.run(debug=True) 