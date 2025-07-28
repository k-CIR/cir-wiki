# VS Code File Explorer Not Visible - Troubleshooting Guide

## Quick Solutions

### 1. Keyboard Shortcut
The fastest way to toggle the file explorer is:
- **Windows/Linux**: `Ctrl + Shift + E`
- **macOS**: `Cmd + Shift + E`

### 2. View Menu
- Go to `View` in the menu bar
- Click on `Explorer` (or `File Explorer`)

### 3. Activity Bar
- Look for the file/folder icon in the left sidebar (Activity Bar)
- If you see it, click on it
- If the Activity Bar is hidden, use `Ctrl/Cmd + Shift + P` and type "View: Toggle Activity Bar"

### 4. Command Palette
- Press `Ctrl/Cmd + Shift + P` to open Command Palette
- Type "Explorer" and select "View: Show Explorer"

### 5. Reset View Locations (Often Works!)
- Press `Ctrl/Cmd + Shift + P` to open Command Palette
- Type "View: Reset View Locations" and select it
- This resets all panel positions to their default locations

## If the Activity Bar is Missing

If you don't see any icons on the left side:

1. **Show Activity Bar**:
   - `View` → `Appearance` → `Activity Bar`
   - Or use Command Palette: "View: Toggle Activity Bar"

2. **Reset Window Layout**:
   - `View` → `Appearance` → `Reset Window Layout`

## Advanced Troubleshooting

### Reset VS Code Settings
If the explorer still doesn't appear:

1. Open Command Palette (`Ctrl/Cmd + Shift + P`)
2. Type "Preferences: Open Settings (JSON)"
3. Look for any settings that might hide the explorer:
   ```json
   "workbench.activityBar.visible": false,
   "explorer.compactFolders": false
   ```

### Workspace Settings
Check if there are workspace-specific settings hiding the explorer:
- Look for a `.vscode/settings.json` file in your project
- Remove any explorer-related hiding settings

## Prevention Tips

- The file explorer can be accidentally hidden by clicking the X button
- Some extensions might modify the layout
- Keyboard shortcuts can accidentally toggle panels

## Still Not Working?

If none of these solutions work:
1. Try restarting VS Code
2. Check if you have any extensions that might be interfering
3. Try opening a different folder/workspace to see if the issue is project-specific