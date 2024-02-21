with source as (
    select *
    from {{ source('main', 'team_players_stats') }}
),

players_metrics as (
    select
        player_name,
        max(age) as current_age,
        sum(games) as total_games_played,
        sum(games_started) as total_games_started,
        sum(minutes_played) as total_minutes_played,
        sum(PTS) as total_points_scored,
        avg(field_percent) as career_avg_field_percent,
        avg(three_percent) as career_three_percent,
        avg(two_percent) as career_two_percent,
        avg(ft_percent) as career_ft_percent,
        sum(trb) as total_rebounds,
        sum(ast) as total_assists,
        sum(blk) as total_blocks,
        sum(tov) as total_turnovers
        
    from mydb.team_players_stats
    
    group by player_name
)

select *
from players_metrics