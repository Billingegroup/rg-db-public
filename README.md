# rg-db-public
Public Research Group Database

Here is an exemplar for the current schema for Institutions.  Below it is the full schema.:

Exemplar:

```
    "institutions": {
        "_id": "columbiau",
        "aka": ["Columbia University", "Columbia"],
        "city": "New York",
        "country": "USA",
        "departments": {
            "physics": {
                "name": "Department of Physics",
                "aka": ["Dept. of Physics", "Physics"],
            },
            "chemistry": {
                "name": "Department of Chemistry",
                "aka": ["Chemistry", "Dept. of Chemistry"],
            },
            "apam": {
                "name": "Department of Applied Physics"
                "and Applied Mathematics",
                "aka": ["APAM"],
            },
        },
        "name": "Columbia University",
        "schools": {
            "seas": {
                "name": "School of Engineering and " "Applied Science",
                "aka": [
                    "SEAS",
                    "Columbia Engineering",
                    "Fu Foundation School of Engineering "
                    "and Applied Science",
                ],
            }
        },
        "state": "NY",
        "zip": "10027",
        "updated": "2020-01-04 16:41:47.790527"
        "uuid": "ff1a6857-76aa-4c23-9758-7bb1aec8b4ed"
    },
```

Full Schema:
```
   "institutions": {
        "_description": {
            "description": "This collection will contain all the institutions"
            "in the world and their departments and addresses"
        },
        "_id": {
            "description": "unique identifier for the institution.",
            "required": True,
            "type": "string",
        },
        "aka": {
            "description": "list of all the different names this "
            "the institution is known by",
            "required": False,
            "type": "list",
        },
        "city": {
            "description": "the city where the institution is",
            "required": True,
            "type": "string",
        },
        "country": {
            "description": "The country where the institution is",
            "required": True,
            "type": "string",
        },
        "departments": {
            "description": "all the departments and centers and"
            "various units in the institution",
            "required": False,
            "type": "dict",
            # Allow unkown department names, but check their content
            "valueschema": {
                "type": "dict",
                "schema": {
                    "name": {
                        "description": "The canonical name",
                        "required": True,
                        "type": "string",
                    },
                    "aka": {"required": False, "type": "list"},
                },
            },
        },
        "name": {
            "description": "the canonical name of the institutions",
            "required": True,
            "type": "string",
        },
        "schools": {
            "description": "this is more for universities, but it "
            "be used for larger divisions in big "
            "organizations",
            "required": False,
            "type": "dict",
            "valueschema": {
                "type": "dict",
                "schema": {
                    "name": {
                        "description": "The canonical name",
                        "required": True,
                        "type": "string",
                    },
                    "aka": {"required": False, "type": "list"},
                },
            },
        },
        "state": {
            "description": "the state where the institution is",
            "required": True,
            "type": "string",
            "dependencies": {"country": "USA"},
        },
        "zip": {
            "description": "the zip or postal code of the institution",
            "required": True,
            "type": "string",
            "dependencies": {"country": "USA"},
        "updated": {
         "description": "The time when the entry was updated",
         "required": false,
         "type": "string",
        },
       "uuid": {
        "description": "A universal ID for the entry",
        "required": false,
        "type": "string"}
        }
        },
    },
```

[![Build Status](https://app.travis-ci.com/Billingegroup/rg-db-public.svg?branch=master)](https://app.travis-ci.com/Billingegroup/rg-db-public)
