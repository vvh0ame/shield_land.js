import requests

class ShieldLand:
	def __init__(self) -> None:
		self.api = "https://api.shield.land"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		self.user_id = None
		self.session_key = None
		self.access_token = None

	def login(
			self,
			email: str,
			password: str) -> dict:
		data = {
			"email": email,
			"password": password
		}
		response = requests.post(
			f"{self.api}/api/auth",
			data=data,
			headers=self.headers).json()
		if "token" in response:
			self.user_id = response["data"]["id"]
			self.access_token = response["token"]
			self.headers["authorization"] = f"Bearer {self.access_token}"
		return response

	def edit_profile(
			self,
			nickname: str = None,
			description: str = None,
			personal_link: str = None) -> dict:
		data = {
			"table": "blog"
		}
		if nickname:
			data["field"] = "name"
			data["value"] = nickname
		elif description:
			data["field"] = "description"
			data["value"] = description
		elif personal_link:
			data["field"] = "code"
			data["value"] = personal_link
		return requests.put(
			f"{self.api}/api/settings/user",
			json=data,
			headers=self.headers).json()

	def get_blocked_users(self) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/get/black-list",
			headers=self.headers).json()

	def get_post_sections(self) -> dict:
		return requests.get(
			f"{self.api}/api/post-sections",
			headers=self.headers).json()

	def get_subscribe_post_sections(self) -> dict:
		return requests.get(
			f"{self.api}/api/post-sections/subscribe",
			headers=self.headers).json()

	def subscribe_post_section(self, section_id: int) -> dict:
		data = {
			"id": section_id
		}
		return requests.post(
			f"{self.api}/api/post-sections/subscribe",
			data=data,
			headers=self.headers).json()

	def change_password(self, password: str) -> dict:
		data = {
			"password": password
		}
		return requests.put(
			f"{self.api}/api/settings/new-password",
			data=data,
			headers=self.headers).json()

	def get_user_profile(self, nickname: str) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/{nickname}",
			headers=self.headers).json()

	def get_user_followers(
			self,
			user_id: int,
			page: int = 1,
			per_page: int = 30,
			sort_by: dict = {"rating": "DESC"},
			subscriptions: int = 1) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/list-register?page={page}&perpage={per_page}&sort_by={sort_by}&subscribers_for={user_id}",
			headers=self.headers).json()

	def get_top_blogs(self) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/get/top-register",
			headers=self.headers).json()

	def follow_blog(self, blog_id: int) -> str:
		data = {
			"blog_id": blog_id
		}
		return requests.post(
			f"{self.api}/api/blogs/get/subscribe",
			data=data,
			headers=self.headers).text

	def unfollow_blog(self, blog_id: int) -> str:
		data = {
			"blog_id": blog_id
		}
		return requests.post(
			f"{self.api}/api/blogs/get/subscribe",
			data=data,
			headers=self.headers).text

	def get_post_likes(self, post_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/post-likes/likes-users?post_id={post_id}",
			headers=self.headers).json()

	def like_post(
			self,
			post_id: int = None,
			comment_id: int = None) -> str:
		data = {}
		if post_id:
			data["post_id"] = post_id
		elif comment_id:
			data["comment_id"] = comment_id
		return requests.put(
			f"{self.api}/api/post-likes/toggle-like",
			data=data,
			headers=self.headers).text

	def unlike_post(
			self,
			post_id: int = None,
			comment_id: int = None) -> str:
		data = {}
		if post_id:
			data["post_id"] = post_id
		elif comment_id:
			data["comment_id"] = comment_id
		return requests.put(
			f"{self.api}/api/post-likes/toggle-like",
			data=data,
			headers=self.headers).text

	def get_post_details(self, post_code: str) -> dict:
		return requests.get(
			f"{self.api}/api/posts/detail/{post_code}",
			headers=self.headers).json()

	def get_post_comments(
			self,
			post_id: int,
			sort: str = "rating") -> dict:
		return requests.get(
			f"{self.api}/api/post-comments/detail?id={post_id}&sort={sort}",
			headers=self.headers).json()

	def get_notifications(self) -> dict:
		return requests.get(
			f"{self.api}/api/notifications/get",
			headers=self.headers).json()

	def get_all_notifications(self) -> dict:
		return requests.get(
			f"{self.api}/api/notifications/get-all",
			headers=self.headers).json()

	def get_order_list(self) -> dict:
		return requests.get(
			f"{self.api}/api/order/list",
			headers=self.headers).json()

	def get_user_info(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/get-info/{user_id}",
			headers=self.headers).json()

	def get_comment_likes(self, comment_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/post-comments/liked-users?comment_id={comment_id}",
			headers=self.headers).json()

	def bookmark_post(self, post_id: int) -> str:
		data = {
			"post_id": post_id
		}
		return requests.post(
			f"{self.api}/api/posts/bookmark",
			data=data,
			headers=self.headers).text

	def unbookmark_post(self, post_id: int) -> str:
		data = {
			"post_id": post_id
		}
		return requests.post(
			f"{self.api}/api/posts/bookmark",
			data=data,
			headers=self.headers).text

	def get_user_characters(self, user_id: int) -> dict:
		return requests.get(
			f"{self.api}/api/characters/list?user_id={user_id}",
			headers=self.headers).json()

	def get_character_pets(self, uuid: str) -> dict:
		return requests.get(
			f"{self.api}/api/pets/{uuid}",
			headers=self.headers).json()

	def get_posts(
			self,
			page: int = 1,
			per_page: int = 20,
			draft: int = 0,
			order_by: dict = {"created_at": "DESC"},
			period: str = "all") -> dict:
		return requests.get(
			f"{self.api}/api/posts/byUser?page={page}&perpage={per_page}&draft={draft}&order_by={order_by}&period={period}",
			headers=self.headers).json()

	def get_categories(self) -> dict:
		return requests.get(
			f"{self.api}/api/categories",
			headers=self.headers).json()

	def get_banners(self) -> dict:
		return requests.get(
			f"{self.api}/api/categories/banners",
			headers=self.headers).json()	

	def get_products(
			self,
			order_by: dict = {"rating": "DESC"}) -> dict:
		return requests.get(
			f"{self.api}/api/products/by-user?order_by={order_by}",
			headers=self.headers).json()

	def get_notifications_count(self) -> dict:
		return requests.get(
			f"{self.api}/api/notifications/get-count",
			headers=self.headers).json()

	def read_notifications(self) -> dict:
		return requests.pot(
			f"{self.api}/api/notifications/read",
			headers=self.headers).json()

	def get_blacklist_blogs(self) -> dict:
		return requests.get(
			f"{self.api}/api/blogs/get/black-list",
			headers=self.headers).json()

	def get_temporal_token(self) -> dict:
		return requests.get(
			f"{self.api}/api/auth/temporal-token",
			headers=self.headers).json()

	def delete_post(self, post_id: int) -> dict:
		data = {
			"post_id": post_id
		}
		return requests.delete(
			f"{self.api}/api/posts",
			data=data,
			headers=self.headers).json()

	def get_routes(self) -> dict:
		return requests.get(
			f"{self.api}/api/routes",
			headers=self.headers).json()

	def get_property_enumerates(self) -> dict:
		return requests.get(
			f"{self.api}/api/property-enum",
			headers=self.headers).json()
			
	
