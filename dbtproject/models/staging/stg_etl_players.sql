with source as (
    select *
    from {{ source('main', 'team_players_stats') }}
),

players as (
    select
        distinct player_name as player_name,
        team as player_team
    from source
)

select *
from players