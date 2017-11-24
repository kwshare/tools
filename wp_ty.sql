-- most views WordPress
SELECT
  post_title,
  meta_value
FROM wp_posts, wp_postmeta
WHERE wp_posts.ID = wp_postmeta.post_id AND post_status = 'publish' AND meta_key = 'views' AND
      (post_type = 'post' OR post_type = 'page')
ORDER BY cast(meta_value AS SIGNED) DESC 


-- most views Typecho
SELECT
  title,
  VIEWS
FROM typecho_contents
WHERE type = 'post' OR type = 'page'
ORDER BY views DESC



-- comments count WordPress
SET @total = (SELECT count(*)
              FROM wp_comments
              WHERE comment_approved = '1');

SET @visitor = (SELECT count(*)
                FROM wp_comments
                WHERE comment_approved = '1' AND user_id != '1');

SET @blogger = (SELECT count(*)
                FROM wp_comments
                WHERE comment_approved = '1' AND user_id = '1');

SELECT
  @total                               AS 'Total',
  @visitor                             AS 'Visitor',
  @blogger                             AS 'Blogger',
  format(@blogger / @visitor * 100, 2) AS 'Percentage';



-- comments count Typecho
SET @total = (SELECT count(*)
              FROM typecho_comments
              WHERE status = 'approved');

SET @visitor = (SELECT count(*)
                FROM typecho_comments
                WHERE status = 'approved' AND authorId != 1);

SET @blogger = (SELECT count(*)
                FROM typecho_comments
                WHERE status = 'approved' AND authorId = 1);


SELECT
  @total                               AS 'Total',
  @visitor                             AS 'Visitor',
  @blogger                             AS 'Blogger',
  format(@blogger / @visitor * 100, 2) AS 'Percentage';