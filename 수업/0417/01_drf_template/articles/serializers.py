from rest_framework import serializers
from .models import Article, Comment

# 목록 조회용 Article Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_field = ('article',)


# 게시글 상세 조회용 Article Serializer 작성
# 게시글 조회할 때, 댓글도 같이 조회하고 싶으면? >> 재정의 overriding
class ArticleDetailSerializer(serializers.ModelSerializer):
    # 게시글이 있을 때 원래는 역참조를 통해 게시물의 댓글을 확인했음
    # 역참조 매니저를 재정의해서 댓글들 직렬화
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        # fields = ('id','title','content')
        fields = '__all__'