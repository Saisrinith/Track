config = {
    "google_api_key": "<your key>",
    "youtube_playlist_id": "PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ",
    "kafka": {
        "bootstrap.servers": "<your serve>",
        "security.protocol": "sasl_ssl",
        "sasl.mechanism": "PLAIN",
        "sasl.username": "<your key>",
        "sasl.password": "<your secret>",
    },
    "schema_registry": {
        "url": "<your SR server>",
        "basic.auth.user.info": "<your SR key>:<your SR secret>",
    }
}