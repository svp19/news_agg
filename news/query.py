from django.db import connection
from django.db.models import Case, When
from news.models import Article, Topic

# Query Statements

q_all_articles = 'select * from news_article;'

q_recent = 'select * from news_article order by id desc limit 6;'

q_topic_views = 'select t.name as topic_id, count(a.id) as num ' \
                'from news_article as a ' \
                'join news_view as v on a.id = v.article_id_id ' \
                'join news_topic as t on a.article_topic_id = t.id ' \
                'where v.user_id_id = %s ' \
                'group by t.name ' \
                'order by count(a.id) desc'

q_article_views = 'select a.id as article_id, t.name as topic_id, count(a.id) as num ' \
                'from news_article as a ' \
                'join news_view as v on a.id = v.article_id_id ' \
                'join news_topic as t on a.article_topic_id = t.id ' \
                'group by a.id, t.name ' \
                'order by count(a.id) desc'


# Raw Query Functions
def get_pragma_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute("PRAGMA table_info(" + table_name + ")")
        row = cursor.fetchall()
    return row


def get_recommended_by_topic(topics):
    with connection.cursor() as cursor:
        # Execute SQL Query
        cursor.execute(q_article_views)
        columns = [col[0] for col in cursor.description]
        result_set = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

        # Pre-process
        topic_article_id_dict = {k.name: [] for k in topics}
        article_views = result_set
        for row in article_views:
            topic_article_id_dict[row['topic_id']].append(row['article_id'])

        topic_article_dict = {}
        for key, value in topic_article_id_dict.items():
            # Preserve order of ids given
            preserved = Case(*[When(id=id, then=pos) for pos, id in enumerate(value)])
            topic_article_dict[key] = Article.objects.filter(id__in=value).order_by(preserved)

    return topic_article_dict


def get_topics_by_preference(user):
    with connection.cursor() as cursor:
        # Execute SQL Query
        cursor.execute(q_topic_views, [user.id])
        topics = []
        for row in cursor.fetchall():
            topics.append(Topic.objects.filter(name=row[0])[0])
    return topics
