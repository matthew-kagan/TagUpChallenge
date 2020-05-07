# Matt Kagan's Tagup Technical Challenge

This is the code for my Tagup Technical Challenge. It is a REST API written in python using the Flask library deployed to Heroku that uses PostgreSQL as a database.

## Base URL
The App is hosted at https://mkagan-tagup-challenge.herokuapp.com/

All endpoints listed below must use above as the base URL. 

## Available endpoints

Route                  |Description|
|--                     |--|
|/api/list              | List all the records|
|/api/create            | Create a record  |
|/api/read/:recordId    | Read a specific record|
|/api/modify/:recordId  | Update a specific record |
|/api/remove/:recordId  | Delete a specific record |

## Request format for creating and updating records

All requests for the create and the modify endpoint must follow the following request format:

```JS
{
  "timestamp": timestamp,
  "value1": value1,
  "value2": value2,
  "value3": value3,
}
```
The timestamp must be an integer representing epoch time.
