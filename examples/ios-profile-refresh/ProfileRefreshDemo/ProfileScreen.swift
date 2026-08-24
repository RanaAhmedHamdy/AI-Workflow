import SwiftUI

struct ProfileScreen: View {
    @ObservedObject var model: ProfileViewModel

    var body: some View {
        VStack(spacing: 16) {
            Text(model.profile.displayName)
                .font(.title)
            Button("Refresh profile") { model.refreshAfterSceneActivation() }
        }
        .padding()
        // SwiftUI cancels this task when the view disappears; it only starts refresh work.
        .task { model.refreshAfterSceneActivation() }
    }
}
