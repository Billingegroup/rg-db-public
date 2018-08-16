***Required fields in people schema for group members

```
    "people": {
        "_description": {
            "description": "This collection describes the members of the "
            "research group.  This is normally public data."
        },
        "_id": {
            "description": "unique identifier for the group member",
            "required": True,
            "type": "string",
        },
        "active": {
            "description": "If the person is an active member, default True.",
            "required": False,
            "type": "boolean",
        },
        "aka": {
            "description": "list of aliases (also-known-as), useful for "
            "identifying the group member in citations or "
            "elsewhere.",
            "required": True,
            "type": ["string", "list"],
        },
        "avatar": {
            "description": "URL to avatar",
            "required": True,
            "type": "string",
        },
        "bio": {
            "description": "short biographical text",
            "required": True,
            "type": "string",
        },
        "collab": {
            "description": "If the person is a collaborator, default False.",
            "required": False,
            "type": "boolean",
        },
        "education": {
            "description": "This contains the educational information for "
            "the group member.",
            "required": True,
            "schema": {
                "type": "dict",
                "schema": {
                    "begin_month": {"required": False, "type": "string"},
                    "begin_year": {"required": True, "type": "integer"},
                    "degree": {"required": True, "type": "string"},
                    "department": {
                        "required": False,
                        "type": "string",
                        "description": "department within" "the institution",
                    },
                    "group": {
                        "required": False,
                        "type": "string",
                        "description": "this employment is/was in"
                        "a group in groups coll",
                    },
                    "end_month": {"required": False, "type": "string"},
                    "end_year": {"required": True, "type": "integer"},
                    "gpa": {"required": False, "type": ("float", "string")},
                    "institution": {"required": True, "type": "string"},
                    "location": {"required": False, "type": "string"},
                    "other": {
                        "required": False,
                        "anyof_type": ["string", "list"],
                    },
                },
            },
            "type": "list",
        },
        "email": {
            "description": "email address of the group member",
            "required": False,
            "type": "string",
        },
        "employment": {
            "description": "Employment information, similar to educational "
            "information.",
            "required": True,
            "schema": {
                "type": "dict",
                "schema": {
                    "begin_month": {"required": False, "type": "string"},
                    "begin_year": {"required": True, "type": "integer"},
                    "end_month": {"required": False, "type": "string"},
                    "end_year": {"required": False, "type": "integer"},
                    "group": {
                        "required": False,
                        "type": "string",
                        "description": "this employment is/was in"
                        "a group in groups coll",
                    },
                    "location": {"required": False, "type": "string"},
                    "organization": {"required": True, "type": "string"},
                    "other": {
                        "required": False,
                        "anyof_type": ["string", "list"],
                    },
                    "position": {"required": True, "type": "string"},
                },
            },
            "type": "list",
        },
        "funding": {
            "description": "Funding and scholarship that the group member "
            "has individually obtained in the past. "
            "**WARNING:** this is not to be confused with the "
            "**grants** collection",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "currency": {"required": False, "type": "string"},
                    "duration": {"required": False, "type": "string"},
                    "month": {"required": False, "type": "string"},
                    "name": {"required": True, "type": "string"},
                    "value": {"required": True, "type": ("float", "integer")},
                    "year": {"required": True, "type": "integer"},
                },
            },
            "type": "list",
        },
        "honors": {
            "description": "Honors that have been awarded to this "
            "group member",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "description": {"required": False, "type": "string"},
                    "month": {"required": False, "type": "string"},
                    "name": {"required": True, "type": "string"},
                    "year": {"required": True, "type": "integer"},
                },
            },
            "type": "list",
        },
        "initials": {
            "description": "The canonical initials for this group member",
            "required": False,
            "type": "string",
        },
        # TODO: include `link`
        "membership": {
            "description": "Professional organizations this member is "
            "a part of",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "begin_month": {"required": False, "type": "string"},
                    "begin_year": {"required": True, "type": "integer"},
                    "description": {"required": False, "type": "string"},
                    "end_month": {"required": False, "type": "string"},
                    "end_year": {"required": False, "type": "integer"},
                    "organization": {"required": True, "type": "string"},
                    "position": {"required": True, "type": "string"},
                    "website": {"required": False, "type": "string"},
                },
            },
            "type": "list",
        },
        "name": {
            "description": "Full, canonical name for the person",
            "required": True,
            "type": "string",
        },
        "position": {
            "description": "such as professor, graduate student, or scientist",
            "required": True,
            "type": "string",
            "eallowed": list(SORTED_POSITION),
        },
        # TODO: need to handle year vs. begin_year stuff
        "service": {
            "description": "Service that this group member has provided",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "description": {"required": False, "type": "string"},
                    "duration": {"required": False, "type": "string"},
                    "month": {"required": False, "type": "string"},
                    "name": {"required": True, "type": "string"},
                    "year": {"required": True, "type": "integer"},
                    "other": {
                        "required": False,
                        "anyof_type": ["string", "list"],
                    },
                },
            },
            "type": "list",
        },
        "skills": {
            "description": "Skill the group member has",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "category": {"required": True, "type": "string"},
                    "level": {"required": True, "type": "string"},
                    "name": {"required": True, "type": "string"},
                },
            },
            "type": "list",
        },
        "teaching": {
            "description": "Courses that this group member has taught, if any",
            "required": False,
            "schema": {
                "type": "dict",
                "schema": {
                    "course": {"required": True, "type": "string"},
                    "description": {"required": False, "type": "string"},
                    "end_month": {"required": False, "type": "string"},
                    "end_year": {"required": False, "type": "integer"},
                    "materials": {"required": False, "type": "string"},
                    "month": {"required": False, "type": "string"},
                    "organization": {"required": True, "type": "string"},
                    "position": {"required": True, "type": "string"},
                    "syllabus": {"required": False, "type": "string"},
                    "video": {"required": False, "type": "string"},
                    "website": {"required": False, "type": "string"},
                    "year": {"required": True, "type": "integer"},
                },
            },
            "type": "list",
        },
        "title": {
            "description": "for example, Dr., etc.",
            "required": False,
            "type": "string",
        },
    },
```
