import Foundation

struct Profile: Codable, Equatable {
    let id: String
    let displayName: String

    static let empty = Profile(id: "local", displayName: "Unnamed profile")
}
