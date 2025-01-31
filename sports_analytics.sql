--Changing data types and adding constraints to the individual columns in the table 

----------categories_table--------

alter table categories_table alter column category_id set data type varchar(50)

alter table categories_table add primary key (category_id) -->adding primary key

alter table categories_table alter column category_name set data type varchar(100)

alter table categories_table alter column category_name set not null 

select * from categories_table


----------competitions_table--------

alter table competitions_table alter column competition_id set data type varchar(50)

alter table competitions_table add primary key (competition_id) -->adding primary key to the column

alter table competitions_table alter column competition_name set data type varchar(100)

alter table competitions_table alter column competition_name set not null 

alter table competitions_table alter column parent_id set data type varchar(50)

alter table competitions_table alter column type set data type varchar(20)

alter table competitions_table alter column type set not null 

alter table competitions_table alter column gender set data type varchar(10)

alter table competitions_table alter column gender set not null

alter table competitions_table alter column category_id set data type varchar(50)

alter table competitions_table add constraint fk_category_id foreign key (category_id) 
references categories_table(category_id)--->adding foreign key

select * from competitions_table


---------------competitor_rankings-------------

alter table competitor_rankings alter column rank_id set data type int

alter table competitor_rankings add primary key (rank_id) -->adding primary key to the column

alter table competitor_rankings alter column rank set data type int

alter table competitor_rankings alter column rank set not null

alter table competitor_rankings alter column movement set data type int

alter table competitor_rankings alter column movement set not null

alter table competitor_rankings alter column points set data type int

alter table competitor_rankings alter column points set not null

alter table competitor_rankings alter column competitions_played set data type int

alter table competitor_rankings alter column competitions_played set not null

alter table competitor_rankings alter column competitor_id set data type varchar(50)

alter table competitor_rankings add constraint fk_competitor_id foreign key (competitor_id)
references competitors_table(competitor_id)  --->adding foreign key

select * from competitor_rankings


------------------competitors_table-----------------

alter table competitors_table alter column competitor_id set data type varchar(50)

alter table competitors_table add primary key(competitor_id)  -->adding primary key to the column

alter table competitors_table alter column name set data type varchar(100)

alter table competitors_table alter column name set not null

alter table competitors_table alter column country set data type varchar(100)

alter table competitors_table alter column country set not null

alter table competitors_table alter column country_code set data type char(3)

update competitors_table set country_code = 'NTL' where country_code IS NULL

alter table competitors_table alter column country_code set not null

alter table competitors_table alter column abbreviation set data type varchar(10)

alter table competitors_table alter column abbreviation set not null

select country from competitors_table where country= 'Neutral'

select * from competitors_table 

---------------------complexes_table -------------

alter table complexes_table alter column complex_id set data type varchar(50)

alter table complexes_table add primary key (complex_id) 

alter table complexes_table alter column complex_name set data type varchar(100)

alter table complexes_table alter column complex_name set not null

select * from complexes_table


-------------venues_table-----------------

alter table venues_table alter column venue_id set data type varchar(50)

alter table venues_table add primary key (venue_id)  

alter table venues_table alter column venue_name set data type varchar(100)

alter table venues_table alter column venue_name set not null

alter table venues_table alter column city_name set data type varchar(100)

alter table venues_table alter column city_name set not null

alter table venues_table alter column country_name set data type varchar(100)

alter table venues_table alter column country_name set not null

alter table venues_table alter column country_code set data type varchar(3)

alter table venues_table alter column country_code set not null

alter table venues_table alter column timezone set data type varchar(100)

alter table venues_table alter column timezone set not null

alter table venues_table alter column complex_id set data type varchar(50)

alter table venues_table add constraint fk_complex_id foreign key (complex_id) references complexes_table(complex_id)

select * from categories_table

select * from  competitions_table

select * from competitor_rankings

select * from competitors_table 

select * from complexes_table

select * from venues_table

select * from tennis_tournaments

select * from points_details

select * from tennis_courts


