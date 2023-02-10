import pytest
from fb_post.interactors.storage_interfaces.dtos import RequestsParametersDTO, \
    UserDto, PostDto, ReactOnPostDto, CommentOnPostDto, CommentOnCommentDto, \
    ReactionOnCommentDto, PostsCountDTO
from fb_post.interactors.presenter_interfaces.dtos import PostDetailsDto
from datetime import datetime
from freezegun import freeze_time
from fb_post.models import User, Post, React, Comment


@pytest.fixture()
def users():
    users = [
        {
            "name": "User 1",
        },
        {
            "name": "User 2",
        },
        {
            "name": "User 3",
        }
    ]

    users_list = []
    for user in users:
        users_list.append(
            User(name=user['name'])
        )
    User.objects.bulk_create(users_list)


@freeze_time("2023-02-08 11:57:29")
@pytest.fixture()
def posts():
    posts_details = [
        {
            "content": "Hello",
            "posted_by_id": "1"
        },
        {
            "content": "Hello 1",
            "posted_by_id": "1"
        },
        {
            "content": "Harsh",
            "posted_by_id": "1"
        },

    ]
    list_posts = []
    for post in posts_details:
        list_posts.append(Post(
            content=post['content'],
            posted_at="2023-02-08 11:57:29",
            posted_by_id=post['posted_by_id']

        ))
    Post.objects.bulk_create(list_posts)


@pytest.fixture()
def request_parameters_dto():
    request_parameters_dto = RequestsParametersDTO(
        offset=0,
        limit=1,
        sort_order="ASC",
        post_content="Hello"
    )
    return request_parameters_dto


@pytest.fixture()
def request_parameters_dto_for_content():
    request_parameters_dto = RequestsParametersDTO(
        offset=0,
        limit=1,
        sort_order="ASC",
        post_content="1"
    )
    return request_parameters_dto


@freeze_time("2023-02-08 11:57:29")
@pytest.fixture()
def posts_details_dto():
    posts_details = [PostDto(
        post_id=1,
        content="Hello",
        posted_at=datetime.now(),
        posted_by_id=1
    )]
    return posts_details


@freeze_time("2023-02-08 11:57:29")
@pytest.fixture()
def posts_details_dto_for_content():
    posts_details = [PostDto(
        post_id=2,
        content="Hello 1",
        posted_at=datetime.now(),
        posted_by_id=1
    )]
    return posts_details




@pytest.fixture()
def get_requests_parameters_dto():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=0, limit=1, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def reacts():
    reacts_obj = React.objects.create(
        post_id=1,
        reaction="HAHA",
        reacted_by_id=1,
        reacted_at=datetime.now()

    )
    reacts_obj.save()
    return reacts_obj


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def reaction_details_dto():
    reactions_details_dto = [ReactOnPostDto(
        reaction_id=1,
        post_id=1,
        reaction="HAHA",
        reacted_by_id=1,
        reacted_at=datetime.now()
    )]
    return reactions_details_dto



@pytest.fixture()
def user_details_dto():
    users_list = [UserDto(user_id=1,
                          name="User 1",
                          profile_pic="www.google.com"
                          )]
    return users_list


@pytest.fixture()
def user():
    user_obj = User.objects.create(name="User 1", profile_pic="www.google.com")
    return user_obj

@pytest.fixture()
def get_requests_parameters_dto_with_invalid_offset():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=-1, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_requests_parameters_dto_with_invalid_limit():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=1, limit=-1, sort_order="", post_content="")
    return get_requests_parameters_dto

@pytest.fixture()
def get_requests_parameters_dto1():
    get_requests_parameters_dto = RequestsParametersDTO(
        offset=0, limit=2, sort_order="", post_content="")
    return get_requests_parameters_dto


@pytest.fixture()
def get_user_dto():
    get_user_dto = UserDto(
        user_id=5,
        name="harsh",
        profile_pic="www.google.com"
    )
    return get_user_dto


@pytest.fixture()
def get_no_posts_dto():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_no_reaction_and_comments_dto():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_reactions():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[ReactOnPostDto(
            reaction_id=1,
            post_id=1,
            reaction="HAHA",
            reacted_at=datetime.now(),
            reacted_by_id=5
        )],
        comments_on_post=[],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments_with_reply():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_with_only_comments_with_reaction():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[ReactionOnCommentDto(
            reaction_id=1,
            reaction="WOW",
            comment_id=1,
            reacted_at=datetime.now(),
            reacted_by_id=5
        )]
    )
    return user_posts_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def get_posts_details():
    user_posts_details_dto = PostDetailsDto(
        users=[UserDto(
            user_id=5,
            name="harsh",
            profile_pic="www.google.com"
        )],
        posts=[PostDto(
            post_id=1,
            content="hello",
            posted_at=datetime.now(),
            posted_by_id=5

        )],
        reactions_on_posts=[ReactOnPostDto(
            reaction_id=1,
            post_id=1,
            reaction="HAHA",
            reacted_at=datetime.now(),
            reacted_by_id=5
        )],
        comments_on_post=[CommentOnPostDto(
            comment_id=1,
            commented_by_id=5,
            content="comment",
            post_id=1,
            commented_at=datetime.now()

        )],
        replies=[CommentOnCommentDto(
            commented_at=datetime.now(),
            comment_id=2,
            commented_by_id=5,
            content="reply",
            parent_comment_id=1
        )],
        reactions_on_comments=[ReactionOnCommentDto(
            reaction_id=1,
            reaction="WOW",
            comment_id=1,
            reacted_at=datetime.now(),
            reacted_by_id=5
        ),
            ReactionOnCommentDto(
                reaction_id=2,
                reaction="SAD",
                comment_id=2,
                reacted_at=datetime.now(),
                reacted_by_id=5,
            )]
    )
    return user_posts_details_dto



@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def posts_details_dto():
    posts_details = [PostDto(
        content="Hello",
        posted_by_id=1,
        posted_at=datetime.now(),
        post_id=1,
    )]
    return posts_details


@pytest.fixture()
def posts2():
    post_obj = Post.objects.create(
        content="Hello",
        posted_by_id=1
    )
    post_obj.save()
    return post_obj





@pytest.fixture()
def request_parameters_dto1():
    request_parameters_dto = RequestsParametersDTO(
        offset=0,
        limit=1,
        sort_order="ASC",
        post_content="Hello"
    )
    return request_parameters_dto




@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def reacts():
    reacts_obj = React.objects.create(
        post_id=1,
        reaction="HAHA",
        reacted_by_id=1,
        reacted_at=datetime.now()

    )
    reacts_obj.save()
    return reacts_obj


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def comments_details_dto():
    comments_details_dto = [CommentOnPostDto(
        comment_id=1,
        content="nice",
        post_id=1,
        commented_at=datetime.now(),
        commented_by_id=1,

    )]
    return comments_details_dto


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def comments():
    comment_obj = Comment.objects.create(
        content="nice",
        commented_by_id=1,
        post_id=1,
        commented_at=datetime.now()
    )
    comment_obj.save()
    return comment_obj


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def reacts_on_comments():
    comment_obj = React.objects.create(
        reaction="HAHA",
        reacted_by_id=1,
        comment_id=1,
        reacted_at=datetime.now()
    )
    comment_obj.save()
    return comment_obj


@pytest.fixture()
@freeze_time("2023-02-08 11:57:29")
def reaction_on_comments_details_dto():
    comments_details_dto = [ReactionOnCommentDto(
        reaction_id=1,
        reaction="HAHA",
        reacted_by_id=1,
        reacted_at=datetime.now(),
        comment_id=1

    )]
    return comments_details_dto


@freeze_time("2023-02-08 11:59:29")
@pytest.fixture()
def posts_details_with_all_filter():
    post_details_dots = [PostDto(
        post_id=1,
        content="Hello",
        posted_by_id=1,
        posted_at=datetime.now()
    )
    ]
    return post_details_dots
