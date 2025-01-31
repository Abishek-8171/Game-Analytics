---categories_table & competitions_table ---

-- 1. List all competitions along with their category name

select competitions_table.competition_name,categories_table.category_name from competitions_table 
inner join categories_table on competitions_table.category_id = categories_table.category_id

-- 2. Count the number of competitions in each category

select categories_table.category_name, count(competitions_table.competition_id) as competition_count
from categories_table join competitions_table on categories_table.category_id = competitions_table.category_id
group by categories_table.category_name order by competition_count desc

-- 3. Find all competitions of type 'doubles'

select competition_name,type from competitions_table where type = 'doubles' 

-- 4.Get competitions that belong to a specific category (e.g., ITF Men)

select competitions_table.competition_name,categories_table.category_name from competitions_table 
inner join categories_table on competitions_table.category_id = categories_table.category_id 
where category_name = 'ITF Men'

-- 5. Identify parent competitions and their sub-competitions

select child.competition_name AS sub_competition,parent.competition_name AS parent_competition
from competitions_table child left join competitions_table parent on child.parent_id = parent.competition_id
order by parent_competition, sub_competition 

-- 6. Analyze the distribution of competition types by category

select  competitions_table.competition_name,categories_table.category_name,count(*) as competition_count
from competitions_table
join categories_table on competitions_table.category_id = categories_table.category_id
group by competition_name, category_name
order by competition_count desc

-- 7. List all competitions with no parent (top-level competitions)

select competition_name,parent_id from competitions_table where parent_id is null

--- Complexes Table & Venues Table ---

-- 1.List all venues along with their associated complex name

select venues_table.venue_name,complexes_table.complex_name from venues_table inner join complexes_table
on venues_table.complex_id = complexes_table.complex_id

-- 2.Count the number of venues in each complex

select complexes_table.complex_name, count(venues_table.venue_name) as venues_count
from venues_table join complexes_table on venues_table.complex_id = complexes_table.complex_id
group by complexes_table.complex_name order by venues_count desc

-- 3.Get details of venues in a specific country (e.g., Chile)

select venue_name,country_name from venues_table where country_name = 'Chile'

-- 4.Identify all venues and their timezones

select timezone,string_agg(venue_name,',') as venues from venues_table group by timezone

select venue_name,timezone from venues_table 

-- 5.Find complexes that have more than one venue

select complexes_table.complex_name, count(venues_table.venue_name) as venues_count
from venues_table join complexes_table on venues_table.complex_id = complexes_table.complex_id
group by complexes_table.complex_name having count (venues_table.venue_name) >= 2  order by venues_count desc

-- 6.List venues grouped by country

select country_name,string_agg(venue_name,',') as venues  from venues_table group by country_name order by country_name

-- 7.Find all venues for a specific complex (e.g., Nacional)

select venues_table.venue_name,complexes_table.complex_name from venues_table inner join complexes_table
on venues_table.complex_id = complexes_table.complex_id where complex_name = 'Nacional'

---------------------- Competitor_Rankings Table & Competitors Table ---------------------


-- 1.Get all competitors with their rank and points.

select competitors_table.name,competitor_rankings.rank,competitor_rankings.points from competitors_table inner join
competitor_rankings on competitor_rankings.competitor_id = competitors_table.competitor_id

-- 2.Find competitors ranked in the top 5

select competitors_table.name,competitor_rankings.rank from competitors_table inner join
competitor_rankings on competitor_rankings.competitor_id = competitors_table.competitor_id 
where rank<= 5 order by rank asc

-- 3.List competitors with no rank movement (stable rank)

select competitors_table.name,competitor_rankings.rank,competitor_rankings.movement from competitors_table inner join
competitor_rankings on competitor_rankings.competitor_id = competitors_table.competitor_id 
where movement = 0 

-- 4.Get the total points of competitors from a specific country (e.g., Croatia)

select competitors_table.name,competitors_table.country,competitor_rankings.points from competitors_table inner join
competitor_rankings on competitor_rankings.competitor_id = competitors_table.competitor_id 
where country = 'Croatia'

-- 5.Count the number of competitors per country

select competitors_table.country, count(competitors_table.name) as competitors_count from competitors_table
group by competitors_table.country order by competitors_count desc

-- 6.Find competitors with the highest points in the current week

select competitors_table.name,competitor_rankings.points from competitors_table inner join
competitor_rankings on competitor_rankings.competitor_id = competitors_table.competitor_id order by points desc


