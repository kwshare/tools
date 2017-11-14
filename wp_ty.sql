SELECT
  post_title,
  meta_value
FROM wp_posts, wp_postmeta
WHERE wp_posts.ID = wp_postmeta.post_id AND meta_key = 'views'
ORDER BY meta_value


SELECT
  title,
  VIEWS
FROM typecho_contents
WHERE type = 'post' OR type = 'page'
ORDER BY views DESC 
