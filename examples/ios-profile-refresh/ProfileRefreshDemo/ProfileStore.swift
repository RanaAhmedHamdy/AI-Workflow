import Foundation

struct ProfileStore {
    private let fileURL: URL

    init(fileURL: URL = URL.documentsDirectory.appending(path: "profile.json")) {
        self.fileURL = fileURL
    }

    func load() -> Profile {
        guard let data = try? Data(contentsOf: fileURL), let profile = try? JSONDecoder().decode(Profile.self, from: data) else {
            return .empty
        }
        return profile
    }

    func save(_ profile: Profile) throws {
        try FileManager.default.createDirectory(at: fileURL.deletingLastPathComponent(), withIntermediateDirectories: true)
        try JSONEncoder().encode(profile).write(to: fileURL, options: .atomic)
    }
}

actor ProfileRefreshService {
    func refresh(existing: Profile) async -> Profile {
        // Deterministic stand-in for an asynchronous client. No network/API key is needed.
        try? await Task.sleep(for: .milliseconds(50))
        return Profile(id: existing.id, displayName: "Ada Lovelace")
    }
}
