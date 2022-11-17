import android.app.Activity;
import android.content.Context;
import android.content.res.Configuration;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewParent;
import android.view.Window;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatCallback;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.appcompat.view.ActionMode;
import com.google.appinventor.components.runtime.AppInventorCompatActivity;
import com.google.appinventor.components.runtime.Form;
import com.google.appinventor.components.runtime.util.PaintUtil;
import com.google.appinventor.components.runtime.util.SdkLevel;
import com.google.appinventor.components.runtime.util.theme.ClassicThemeHelper;
import com.google.appinventor.components.runtime.util.theme.HoneycombThemeHelper;
import com.google.appinventor.components.runtime.util.theme.IceCreamSandwichThemeHelper;
import com.google.appinventor.components.runtime.util.theme.ThemeHelper;

class AppInventorCompatActivity
extends Activity
implements AppCompatCallback {
    static final int DEFAULT_PRIMARY_COLOR;
    private static final String LOG_TAG;
    private static boolean actionBarEnabled;
    private static boolean classicMode;
    private static Theme currentTheme;
    private static boolean didSetClassicModeFromYail;
    private static int primaryColor;
    private AppCompatDelegate appCompatDelegate;
    LinearLayout frameWithTitle;
    protected ThemeHelper themeHelper;
    TextView titleBar;

    static {
        LOG_TAG = AppInventorCompatActivity.class.getSimpleName();
        DEFAULT_PRIMARY_COLOR = PaintUtil.hexStringToInt((String)"&HFF3F51B5");
        classicMode = false;
        currentTheme = Theme.PACKAGED;
        didSetClassicModeFromYail = false;
    }

    private void applyTheme() {
        Log.d((String)LOG_TAG, (String)("applyTheme " + (Object)currentTheme));
        this.setClassicMode(false);
        switch (1.$SwitchMap$com$google$appinventor$components$runtime$AppInventorCompatActivity$Theme[currentTheme.ordinal()]) {
            default: {
                return;
            }
            case 1: {
                this.setClassicMode(true);
                this.setTheme(16973829);
                return;
            }
            case 2: 
            case 3: {
                this.setTheme(16974124);
                return;
            }
            case 4: 
        }
        this.setTheme(16974121);
    }

    protected static int getPrimaryColor() {
        return primaryColor;
    }

    protected static boolean isActionBarEnabled() {
        return actionBarEnabled;
    }

    public static boolean isClassicMode() {
        return classicMode;
    }

    public static boolean isEmulator() {
        return Build.PRODUCT.contains((CharSequence)"google_sdk") || Build.PRODUCT.equals((Object)"sdk") || Build.PRODUCT.contains((CharSequence)"sdk_gphone");
    }

    public static void setClassicModeFromYail(boolean bl) {
        if (!didSetClassicModeFromYail) {
            Log.d((String)LOG_TAG, (String)("Setting classic mode from YAIL: " + bl));
            classicMode = bl;
            didSetClassicModeFromYail = true;
        }
    }

    /*
     * Enabled aggressive block sorting
     */
    private boolean shouldCreateTitleBar() {
        return this.isAppCompatMode() && (!this.themeHelper.hasActionBar() || !AppInventorCompatActivity.isActionBarEnabled()) || this.titleBar == null && (this.isRepl() || classicMode);
    }

    public ActionBar getSupportActionBar() {
        block3 : {
            Window.Callback callback = this.getWindow().getCallback();
            try {
                if (this.appCompatDelegate != null) break block3;
                return null;
            }
            catch (IllegalStateException illegalStateException) {
                this.appCompatDelegate = null;
                classicMode = true;
                this.getWindow().setCallback(callback);
                return null;
            }
        }
        ActionBar actionBar = this.appCompatDelegate.getSupportActionBar();
        return actionBar;
    }

    protected void hideTitleBar() {
        block5 : {
            block4 : {
                if (this.titleBar == null) break block4;
                if (this.titleBar.getParent() == this.frameWithTitle) break block5;
                if (this.titleBar.getParent() != null) {
                    ((View)this.titleBar.getParent()).setVisibility(8);
                }
            }
            return;
        }
        this.titleBar.setVisibility(8);
    }

    public final boolean isAppCompatMode() {
        return this.appCompatDelegate != null;
    }

    public boolean isRepl() {
        return false;
    }

    protected void maybeShowTitleBar() {
        if (this.titleBar != null) {
            this.titleBar.setVisibility(0);
            Log.d((String)LOG_TAG, (String)"titleBar visible");
            if (this.titleBar.getParent() != null && this.titleBar.getParent() != this.frameWithTitle) {
                Log.d((String)LOG_TAG, (String)"Setting parent visible");
                ((View)this.titleBar.getParent()).setVisibility(0);
            }
        }
    }

    public void onConfigurationChanged(Configuration configuration) {
        super.onConfigurationChanged(configuration);
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.onConfigurationChanged(configuration);
        }
    }

    /*
     * Enabled aggressive block sorting
     */
    public void onCreate(Bundle bundle) {
        boolean bl = classicMode || SdkLevel.getLevel() < 11;
        if (classicMode = bl) {
            this.themeHelper = new ClassicThemeHelper();
        } else if (SdkLevel.getLevel() < 14) {
            this.themeHelper = new HoneycombThemeHelper(this);
            this.themeHelper.requestActionBar();
            actionBarEnabled = true;
        } else {
            this.themeHelper = new IceCreamSandwichThemeHelper(this);
            if (currentTheme != Theme.PACKAGED) {
                this.applyTheme();
            }
            this.appCompatDelegate = AppCompatDelegate.create((Activity)this, (AppCompatCallback)this);
            this.appCompatDelegate.onCreate(bundle);
        }
        super.onCreate(bundle);
        this.frameWithTitle = new LinearLayout((Context)this);
        this.frameWithTitle.setOrientation(1);
        this.setContentView((View)this.frameWithTitle);
        actionBarEnabled = this.themeHelper.hasActionBar();
        this.titleBar = (TextView)this.findViewById(16908310);
        if (!this.shouldCreateTitleBar()) {
            Log.d((String)LOG_TAG, (String)("Already have a title bar (classic mode): " + (Object)this.titleBar));
            return;
        }
        this.titleBar = new TextView((Context)this);
        this.titleBar.setBackgroundResource(17301653);
        this.titleBar.setTextAppearance((Context)this, 16973907);
        this.titleBar.setGravity(16);
        this.titleBar.setSingleLine();
        this.titleBar.setShadowLayer(2.0f, 0.0f, 0.0f, -1157627904);
        if (!AppInventorCompatActivity.isClassicMode() || SdkLevel.getLevel() < 11) {
            this.frameWithTitle.addView((View)this.titleBar, new ViewGroup.LayoutParams(-1, -2));
        }
    }

    protected void onDestroy() {
        super.onDestroy();
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.onDestroy();
        }
    }

    protected void onPostCreate(Bundle bundle) {
        super.onPostCreate(bundle);
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.onPostCreate(bundle);
        }
    }

    protected void onPostResume() {
        super.onPostResume();
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.onPostResume();
        }
    }

    protected void onStop() {
        super.onStop();
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.onStop();
        }
    }

    public void onSupportActionModeFinished(ActionMode actionMode) {
    }

    public void onSupportActionModeStarted(ActionMode actionMode) {
    }

    /*
     * Enabled aggressive block sorting
     */
    protected void onTitleChanged(CharSequence charSequence, int n) {
        super.onTitleChanged(charSequence, n);
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.setTitle(charSequence);
            return;
        } else {
            if (this.titleBar == null) return;
            {
                this.titleBar.setText(charSequence);
                return;
            }
        }
    }

    @Nullable
    public ActionMode onWindowStartingSupportActionMode(ActionMode.Callback callback) {
        return null;
    }

    protected void setActionBarEnabled(boolean bl) {
        actionBarEnabled = bl;
    }

    /*
     * Enabled aggressive block sorting
     */
    protected void setAppInventorTheme(Theme theme) {
        if (!Form.getActiveForm().isRepl() || theme == currentTheme) {
            return;
        }
        currentTheme = theme;
        this.applyTheme();
    }

    protected void setClassicMode(boolean bl) {
        if (this.isRepl() && SdkLevel.getLevel() >= 11) {
            classicMode = bl;
        }
    }

    public void setContentView(View view) {
        if (view != this.frameWithTitle) {
            this.frameWithTitle.addView(view, (ViewGroup.LayoutParams)new FrameLayout.LayoutParams(-1, -1));
            view = this.frameWithTitle;
        }
        if (this.appCompatDelegate != null) {
            this.appCompatDelegate.setContentView(view);
            return;
        }
        super.setContentView(view);
    }

    /*
     * Enabled aggressive block sorting
     */
    protected void setPrimaryColor(int n) {
        ActionBar actionBar = this.getSupportActionBar();
        int n2 = n == 0 ? DEFAULT_PRIMARY_COLOR : n;
        if (actionBar != null && n2 != primaryColor) {
            primaryColor = n2;
            actionBar.setBackgroundDrawable((Drawable)new ColorDrawable(n));
        }
    }

    /*
     * Enabled aggressive block sorting
     */
    protected void styleTitleBar() {
        ActionBar actionBar = this.getSupportActionBar();
        Log.d((String)LOG_TAG, (String)("actionBarEnabled = " + actionBarEnabled));
        String string2 = LOG_TAG;
        StringBuilder stringBuilder = new StringBuilder().append("!classicMode = ");
        boolean bl = !classicMode;
        Log.d((String)string2, (String)stringBuilder.append(bl).toString());
        Log.d((String)LOG_TAG, (String)("actionBar = " + (Object)actionBar));
        if (actionBar != null) {
            actionBar.setBackgroundDrawable((Drawable)new ColorDrawable(AppInventorCompatActivity.getPrimaryColor()));
            if (actionBarEnabled) {
                actionBar.show();
                this.hideTitleBar();
                return;
            }
            actionBar.hide();
        }
        this.maybeShowTitleBar();
    }
}