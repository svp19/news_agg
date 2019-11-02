# Queries

q_all = 'select * from news_article;'
q_recent = 'select * from news_article order by id desc limit 6;'

q_article_views = 'select * from news_article natural join news_view;'
