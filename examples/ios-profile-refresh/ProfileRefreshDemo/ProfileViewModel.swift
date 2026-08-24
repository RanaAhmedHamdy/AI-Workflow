import Foundation

@MainActor
final class ProfileViewModel: ObservableObject {
    @Published private(set) var profile: Profile
    private let store: ProfileStore
    private let refreshService: ProfileRefreshService
    private var refreshTask: Task<Void, Never>?

    init(store: ProfileStore = ProfileStore(), refreshService: ProfileRefreshService = ProfileRefreshService()) {
        self.store = store
        self.refreshService = refreshService
        self.profile = store.load()
    }

    func refreshAfterSceneActivation() {
        refreshTask?.cancel()
        refreshTask = Task { [weak self, store, refreshService] in
            guard let self else { return }
            let refreshed = await refreshService.refresh(existing: self.profile)
            guard !Task.isCancelled else { return }
            try? store.save(refreshed)
            self.profile = refreshed
        }
    }

    deinit { refreshTask?.cancel() }
}
