from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

from app.api.helpers.utilities import dasherize


class FeedbackSchema(Schema):
    """
    Api schema for Feedback Model
    """
    class Meta:
        """
        Meta class for Feedback Api Schema
        """
        type_ = 'feedback'
        self_view = 'v1.feedback_detail'
        self_view_kwargs = {'id': '<id>'}
        inflect = dasherize

    id = fields.Str(dump_only=True)
    rating = fields.Str(required=True)
    comment = fields.Str(required=False)
    event = Relationship(attribute='event',
                         self_view='v1.feedback_event',
                         self_view_kwargs={'id': '<id>'},
                         related_view='v1.event_detail',
                         related_view_kwargs={'feedback_id': '<id>'},
                         schema='EventSchemaPublic',
                         type_='event')
    user = Relationship(attribute='user',
                        self_view='v1.feedback_user',
                        self_view_kwargs={'id': '<id>'},
                        related_view='v1.user_detail',
                        related_view_kwargs={'feedback_id': '<id>'},
                        schema='UserSchema',
                        type_='user'
                        )
