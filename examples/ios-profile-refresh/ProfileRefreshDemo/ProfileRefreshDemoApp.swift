import SwiftUI

@main
struct ProfileRefreshDemoApp: App {
    @StateObject private var model = ProfileViewModel()
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            ProfileScreen(model: model)
                .onChange(of: scenePhase) { _, phase in
                    guard phase == .active else { return }
                    model.refreshAfterSceneActivation()
                }
        }
    }
}
