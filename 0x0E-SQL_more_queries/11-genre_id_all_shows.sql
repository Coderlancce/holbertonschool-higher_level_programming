-- Import the database dump of hbtn_0d_tvshows to your MySQL
-- server: download (same as 10-genre_id_by_show.sql)

SELECT sh.title, shgr.genre_id FROM tv_shows AS sh
       LEFT JOIN tv_show_genres AS shgr ON sh.id=shgr.show_id
       ORDER BY sh.title, shgr.genre_id ASC;
