# Ayomi technical test

## How to run

```shell script
$ docker-compose build
$ ./manage migrate
$ docker-compose up
```

## Notes

- I have used Django's auth module instead of creating my own User models
- I have added some extra fields to play around with the Form system a bit
- `./manage` is a convenience one-liner script for bash to access manage.py inside the container
- Due to docker-compose not waiting for dependencies there might be a small issue with the migration script, run `docker-compose up -d db` before migration to avoid issue
