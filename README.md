# Restaurant

A toy backend for a restaurant, including an admin site and JSON API for a mobile app.

The admin site at `admin/` provides menu editing and changing orders' status capabilities.

![](https://i.imgur.com/PmOIkp6.png)

There are JSON API endpoints for authentication, getting the menu and posting an order.

### Authentication

The `obtain_auth_token` view at `api-token-auth/` will return a JSON response when valid `username` and `password` fields are POSTed to the view using form data or JSON:

```JSON
{ "token" : "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" }
```

For clients to authenticate, the token key should be included in the `Authorization` HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Getting the menu

`GET` at `orders/menu/` returns a JSON with a forest of category trees. For example,

```JSON
[
    {
        "name": "Pizza",
        "dishes": [
            {
                "id": 1,
                "name": "Margarita",
                "price": 250
            }
        ],
        "subcategories": []
    },
    {
        "name": "Pasta",
        "dishes": [
            {
                "id": 2,
                "name": "Pasta Bolognese",
                "price": 300
            }
        ],
        "subcategories": []
    },
    {
        "name": "Drinks",
        "dishes": [],
        "subcategories": [
            {
                "name": "Tea",
                "dishes": [
                    {
                        "id": 6,
                        "name": "Green Tea",
                        "price": 100
                    }
                ],
                "subcategories": []
            },
            {
                "name": "Coffee",
                "dishes": [
                    {
                        "id": 7,
                        "name": "Latte",
                        "price": 150
                    },
                    {
                        "id": 8,
                        "name": "Cappuccino",
                        "price": 150
                    }
                ],
                "subcategories": []
            }
        ]
    }
]
```

### Posting an order

`POST` at `orders/post/` a JSON with a `restaurant` id and `items` array, consisting of `dish` ids and counts. Total is calculated automatically at order creation using current dish prices (which can change any time).

Example:

```JSON
{
	"restaurant": 1,
	"items": [
			{
				"dish": 7,
				"count": 2
			},
			{
				"dish": 1,
				"count": 2
			},
			{
				"dish": 6,
				"count": 1
			}
		]
}
```
