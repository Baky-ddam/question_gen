/**
 * EYESH Question Generator - API Client
 */

const API = {
    baseUrl: '/api',

    async request(endpoint, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        };

        try {
            const response = await fetch(url, config);
            if (!response.ok) {
                const error = await response.json().catch(() => ({ detail: 'Unknown error' }));
                throw new Error(error.detail || `HTTP ${response.status}`);
            }
            return await response.json();
        } catch (e) {
            console.error('API Error:', e);
            throw e;
        }
    },

    // Health & Stats
    async getHealth() {
        return this.request('/health');
    },

    async getStats() {
        return this.request('/stats');
    },

    // Patterns
    async getPatterns({ level, focus, domain, page = 1, limit = 50 } = {}) {
        const params = new URLSearchParams();
        if (level) params.append('level', level);
        if (focus) params.append('focus', focus);
        if (domain) params.append('domain', domain);
        params.append('page', page);
        params.append('limit', limit);
        return this.request(`/patterns?${params}`);
    },

    async getPattern(patternId) {
        return this.request(`/patterns/${encodeURIComponent(patternId)}`);
    },

    async getFocuses() {
        return this.request('/patterns/focus/list');
    },

    async getLevels() {
        return this.request('/patterns/level/list');
    },

    async getDomains() {
        return this.request('/patterns/domain/list');
    },

    // Exams
    async generateExam({ count = 10, level = null, pattern_id = null, mode = 'user' } = {}) {
        return this.request('/exams/generate', {
            method: 'POST',
            body: JSON.stringify({ count, level, pattern_id, mode })
        });
    },

    async submitExam({ exam_id, answers }) {
        return this.request('/exams/submit', {
            method: 'POST',
            body: JSON.stringify({ exam_id, answers })
        });
    }
};
