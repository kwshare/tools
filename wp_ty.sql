SELECT
  post_title,
  meta_value
FROM wp_posts, wp_postmeta
WHERE wp_posts.ID = wp_postmeta.post_id AND post_status = 'publish' AND meta_key = 'views' AND
      (post_type = 'post' OR post_type = 'page')
ORDER BY cast(meta_value AS SIGNED) DESC 


SELECT
  title,
  VIEWS
FROM typecho_contents
WHERE type = 'post' OR type = 'page'
ORDER BY views DESC 
