class ShieldLand {
	constructor() {
		this.api = "https://api.shield.land/api"
		this.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
	}

	async login(email, password) {
		const response = await fetch(
			`${this.api}/auth`, {
				method: "POST",
				body: JSON.stringify({
					email: email,
					password: password
				}),
				headers: this.headers
			})
		const data = await response.json()
		if ("token" in data) {
			this.userId = data.data.id
			this.accessToken = data.data.token
			this.headers["authorization"] = `Bearer ${this.accessToken}`
		}
		return data
	}

	
	async editProfile(nickname = null, description = null, personalLink = null) {
		let body = {table: "blog"}
		if (nickname) {
			body.field = "name"
			body.value = nickname
		} else if (description) {
			body.field = "description"
			body.value = description
		} else if (personalLink) {
			body.field = "code"
			body.value = personalLink
		}
		const response = await fetch(
			`${this.api}/settings/user`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async getBlockedUsers() {
		const response = await fetch(
			`${this.api}/blogs/get/black-list`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPostSections() {
		const response = await fetch(
			`${this.api}/post-sections`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getSubscribePostSections() {
		const response = await fetch(
			`${this.api}/post-sections/subscribe`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async subscribePostSection(sectionId) {
		const response = await fetch(
			`${this.api}/post-sections/subscribe`, {
				method: "POST",
				body: JSON.stringify({
					id: sectionId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async changePassword(password) {
		const response = await fetch(
			`${this.api}/settings/new-password`, {
				method: "POST",
				body: JSON.stringify({
					password: password
				}),
				headers: this.headers
			})
		return response.json()
	}


	async getUserBloga(nickname) {
		const response = await fetch(
			`${this.api}/blogs/${nickname}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserFollowers(
			userId,
			page = 1,
			perPage = 30,
			sortBy = {"rating": "DESC"},
			subscriptions = 1) {
		const response = await fetch(
			`${this.api}/blogs/list-register?page=${page}&perpage=${perPage}&sort_by=${sortBy}&subscribers_for=${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTopBlogs() {
		const response = await fetch(
			`${this.api}/blogs/get/top-register`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async followBlog(blogId) {
		const response = await fetch(
			`${this.api}/blogs/get/subscribe`, {
				method: "POST",
				body: JSON.stringify({
					blog_id: blogId
				}),
				headers: this.headers
			})
		return response.text()
	}

	async getPostLikes(postId) {
		const response = await fetch(
			`${this.api}/post-likes/likes-users?post_id=${postId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async likePost(postId) {
		const response = await fetch(
			`${this.api}/post-likes/toggle-like`, {
				method: "POST",
				body: JSON.stringify({
					post_id: postId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getPostInfo(postCode) {
		const response = await fetch(
			`${this.api}/posts/detail/${postCode}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPostComments(postId, sort = "rating") {
		const response = await fetch(
			`${this.api}/post-comments/detail?id=${postId}&sort=${sort}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getNotifications() {
		const response = await fetch(
			`${this.api}/notifications/get-all`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserInfo(userId) {
		const response = await fetch(
			`${this.api}/blogs/get-info/${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async bookMarkPost(postId) {
		const response = await fetch(
			`${this.api}/posts/bookmark`, {
				method: "POST",
				body: JSON.stringify({
					post_id: postId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getUserCharacters(userId) {
		const response = await fetch(
			`${this.api}/characters/list?user_id=${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCharacterPets(uuid) {
		const response = await fetch(
			`${this.api}/pets/${uuid}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPosts(
			page = 1,
			perPage = 30,
			draft = 0,
			oderBy = {"created_at": "DESC"},
			period = "all") {
		const response = await fetch(
			`${this.api}/posts/byUser?page=${page}&perpage=${perPage}&draft=${draft}&order_by=${orderBy}&period=${period}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCategories() {
		const response = await fetch(
			`${this.api}/categories`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBanners() {
		const response = await fetch(
			`${this.api}/categories/banners`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getProducts(orderBy = {"rating": "DESC"}) {
		const response = await fetch(
			`${this.api}/products/by-user?order_by=${orderBy}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getTemporalToken() {
		const response = await fetch(
			`${this.api}/auth/temporal-token`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRoutes() {
		const response = await fetch(
			`${this.api}/routes`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPropertyEnumerates() {
		const response = await fetch(
			`${this.api}/property-enum`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {ShieldLand}
