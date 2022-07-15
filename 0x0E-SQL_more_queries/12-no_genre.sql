-- Import the database dump from hbtn_0d_tvshows to your
-- MySQL server: download (same as 11-genre_id_all_shows.sql)

SELECT sh.title, shgr.genre_id FROM tv_shows sh
       LEFT JOIN tv_show_genres shgr ON sh.id=shgr.show_id
       WHERE shgr.genre_id IS NULL
       ORDER BY sh.title, shgr.genre_id ASC;
